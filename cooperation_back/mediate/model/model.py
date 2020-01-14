from contextlib import contextmanager

from pymongo.errors import DuplicateKeyError

from ..helpers import get_now, get_uuid
from ..i18n import I18N
from ..errors import *

from .base import BaseModel
from .field import Reserved


class Model(BaseModel, metaclass=BaseModel.Meta):
    """
        mongo orm model
        """

    class Null:
        """
        We are using python None for empty field(to delete),
        so we have to have another value representing null in json object.
        """
        pass

    mongo_id = Reserved(mongo_field='_id')
    created_at = Reserved(mongo_field='created_at')
    updated_at = Reserved(mongo_field='updated_at')
    deleted_at = Reserved(mongo_field='deleted_at')

    coll_name = None

    def __init__(self, mongo_db=None, coll_name=None, i18n: I18N = None):
        """
        init a model

        :param i18n: internationalization
        :param mongo_db: mongo db object
        :param coll_name: collection name
        """
        super().__init__()
        self._with_deleted = False

        self.i18n = i18n or I18N()
        self.mongo_db = None
        self.coll = None
        if mongo_db is not None or coll_name is not None:
            self.setup(mongo_db, coll_name)

    def setup(self, mongo_db, coll_name):
        if mongo_db is not None and self.mongo_db is None:
            self.mongo_db = mongo_db
        if coll_name is not None:
            self.coll_name = coll_name
        self.coll = mongo_db[self.coll_name]

    @property
    @contextmanager
    def handle_deleted(self):
        self._with_deleted = True
        yield
        self._with_deleted = False

    def copy(self):
        self_class = type(self)
        copied = self_class(mongo_db=self.mongo_db, coll_name=self.coll_name, i18n=self.i18n)
        copied.reserved_fields = self.reserved_fields.copy()
        copied.normal_fields = self.normal_fields.copy()
        copied.values = self.values.copy()
        return copied

    @property
    def id(self):
        return self.mongo_id

    async def from_id(self, mongo_id=None, extra_query=None, to_raise=True):
        """
        get a mongo object from id

        :param mongo_id: the id in mongo database
        :param extra_query: mongo project
        :param to_raise:
        :return:
        """
        if mongo_id is None:
            mongo_id = self.mongo_id
        query = {'_id': mongo_id}
        if extra_query is not None:
            query = {"$and": [query, extra_query]}
        obj = await self.coll.find_one(query)
        if obj is None or (not self._with_deleted and obj.get("deleted_at") is not None):
            if to_raise:
                raise NONEXISTENT_MONGO_ID(
                    reason=self.i18n.nonexistent_id % mongo_id
                )
            return None
        self.clear()
        self.values.update(obj)
        return self

    async def find_one(self, query=None, to_raise=True):
        """
        get a mongo object from id

        :param query: mongo project
        :param to_raise:
        :return:
        """
        obj = await self.coll.find_one(query)
        if obj is None or (not self._with_deleted and obj.get("deleted_at") is not None):
            if to_raise:
                raise NO_RECORD(
                    reason=self.i18n.no_record
                )
            return None
        self.clear()
        self.values.update(obj)
        return self

    def find(
            self,
            query=None,
            project=None,
            limit=None,
            skip=None,
            sort=None,
            extra_filter=None
    ):
        if not self._with_deleted:
            query = {"$and": [query, {"deleted_at": None}]}
        cursor = Cursor(
            i18n=self.i18n,
            coll=self.coll,
            query=query,
            project=project,
            limit=limit,
            skip=skip,
            sort=sort,
            extra_filter=extra_filter,
            model_class=type(self))
        return cursor

    async def save(self, data=None, with_reserved=False, updated_at=None, **kwargs):
        """
        save a model

        :param data: specify the data to save
        :param with_reserved: set True to save with_reserved fields
        :param updated_at: specify the data to save
        :return:
        """

        if data is None:
            data = dict()
        data.update(kwargs)

        if len(data) == 0:
            data = self.values.copy()
        else:
            for key, value in data.items():
                if value is self.Null:
                    self.values[key] = None
                elif value is None:
                    if key in self.values:
                        self.values.pop(key)
                else:
                    self.values[key] = value

        if not self.has_extra:
            to_pop = set()

            for key in data:
                if key not in self.fields:
                    to_pop.add(key)
            for one in to_pop:
                data.pop(one)

        if not with_reserved:
            for reserved in self.reserved_fields:
                if reserved in data:
                    data.pop(reserved)

        set_query = dict()
        unset_query = dict()
        for key, value in data.items():
            if value is None:
                unset_query[key] = ''
                if key in self:
                    self.values.pop(key)
            else:
                if value is self.Null:
                    value = None
                set_query[key] = value

        if set_query or unset_query:
            set_query['updated_at'] = get_now().isoformat()

        query = dict()
        if set_query:
            query['$set'] = set_query
        if unset_query:
            query['$unset'] = unset_query
        if query:
            await self.mongo_update(query, updated_at)

    async def delete(self):
        """
        delete a model by id

        :return:
        """
        await self.coll.delete_one({'_id': self.mongo_id})

    async def delete_many(self, query):
        """
        delete a model by id

        :return:
        """
        await self.coll.delete_many(query)

    async def soft_delete(self):
        """
        soft delete
        :return:
        """
        await self.save(
            with_reserved=True,
            deleted_at=get_now().isoformat()
        )

    async def soft_delete_many(self, query):
        """
        soft delete
        :return:
        """
        await self.coll.update_many(
            query,
            {'$set': {'created_at': get_now().isoformat()}},
        )

    async def restore(self):
        await self.save(
            with_reserved=True,
            deleted_at=None
        )

    async def create(self, data=None, **kwargs):
        """
        create a new model

        :param data:
        :param kwargs:
        :return:
        """
        if data is None:
            data = dict()

        data.update(kwargs)
        data['created_at'] = get_now().isoformat()

        none_keys = set()
        for key, value in data.items():
            if value is self.Null:
                none_keys.add(key)

        for key in none_keys:
            data[key] = None

        if '_id' not in data:
            data['_id'] = get_uuid()
        try:
            await self.coll.insert_one(data)
        except DuplicateKeyError as exception:
            raise DUPLICATED_MONGO_KEY(reason=self.i18n.duplicated_mongo_key % exception)
        self.clear()
        for k, v in data.items():
            self.values[k] = v
        return self

    async def mongo_update(self, ops, updated_at=None):
        """
        update an object with origin mongo operations

        :param ops: mongo ops
        :param updated_at: update lock
        :return:
        """
        mongo_filter = {'_id': self.mongo_id}
        if not self._with_deleted:
            mongo_filter["deleted_at"] = None
        if updated_at is not None:
            mongo_filter['updated_at'] = self.updated_at
        try:
            result = await self.coll.update_one(mongo_filter, ops)
        except DuplicateKeyError as exception:
            raise DUPLICATED_MONGO_KEY(reason=self.i18n.duplicated_mongo_key % exception)
        if updated_at is not None and result.modified_count == 0:
            raise MODIFY_OUTDATED_DOCUMENT

    def __hash__(self):
        return hash(self.id)

    @property
    def allow_extra(self):
        @contextmanager
        def with_extra():
            old_status = self.has_extra
            self.has_extra = True
            yield
            self.has_extra = old_status
        return with_extra()


class Cursor:
    """
    Cursor is used to describe how to go through a collection
    """

    def __init__(
            self,
            coll,
            query=None,
            project=None,
            limit=None,
            skip=None,
            sort=None,
            extra_filter=None,
            model_class=Model,
            i18n: I18N = None
    ):
        self.i18n = i18n or I18N()
        if query is None:
            query = dict()
        if sort is None:
            sort = [('_id', 1)]
        self.coll = coll
        self.querying = query
        self.projection = project
        self.limiting = limit
        self.skipping = skip
        self.sorting = sort
        self.model_class = model_class
        if extra_filter is None:
            async def extra_filter(cursor):
                async for x in cursor:
                    record = self.model_class(
                        i18n=self.i18n,
                        mongo_db=self.coll.database,
                        coll_name=coll.name
                    )
                    record.values.update(x)
                    yield record
        self.extra_filter = extra_filter
        pass

    def query(self, query):
        self.querying = query
        return self

    def project(self, project):
        self.projection = project
        return self

    def skip(self, skip):
        self.skipping = skip
        return self

    def limit(self, limit):
        self.limiting = limit
        return self

    def sort(self, sort):
        self.sorting = sort
        return self

    def append_filter(self, extra_filter=lambda x: x):
        self_class = type(self)
        cursor = self_class(
            i18n=self.i18n,
            coll=self.coll,
            query=self.querying,
            project=self.projection,
            limit=self.limiting,
            skip=self.skipping,
            sort=self.sorting,
            extra_filter=lambda x: extra_filter(self.extra_filter(x)),
            model_class=self.model_class
        )
        return cursor

    def mongo_cursor(self):
        cursor = self.coll.find(self.querying, self.projection)
        if self.limiting is not None:
            cursor.limit(self.limiting)
        if self.skipping is not None:
            cursor.skip(self.skipping)
        if self.sorting is not None:
            cursor.sort(self.sorting)
        return cursor

    async def count(self):
        return await self.coll.count_documents(self.querying)

    async def walk(self):
        async for x in self.extra_filter(self.mongo_cursor()):
            yield x

    def __aiter__(self):
        return self.walk()
