import datetime

import dateutil.parser as datetime_parser

from ..helpers import get_now


class Field:
    reserved = False

    def __init__(self, mongo_field: str, unique=False):
        self.mongo_field = mongo_field
        self.unique = unique

    def from_repr(self, repr_data):
        return repr_data

    @staticmethod
    def to_repr(value):
        return value

    def __get__(self, instance, owner):
        return self.from_repr(instance.values[self.mongo_field])

    def __set__(self, instance, value):
        instance.values[self.mongo_field] = self.to_repr(value)


class Reserved(Field):
    reserved = True


class Normal(Field):
    pass


class IntField(Normal):
    def from_repr(self, repr_data):
        if not isinstance(repr_data, int):
            raise TypeError(f"The type of {self.mongo_field} should be int")


class FloatField(Normal):
    def from_repr(self, repr_data):
        if not isinstance(repr_data, float):
            raise TypeError(f"The type of {self.mongo_field} should be float")


class StrField(Normal):
    def from_repr(self, repr_data):
        if not isinstance(repr_data, str):
            raise TypeError(f"The type of {self.mongo_field} should be str")


class BoolField(Normal):
    def from_repr(self, repr_data):
        if not isinstance(repr_data, bool):
            raise TypeError(f"The type of {self.mongo_field} should be str")


class IDField(Normal):
    def from_repr(self, repr_data):
        if not isinstance(repr_data, str):
            raise TypeError(f"The type of {self.mongo_field} should be str")


class DateTimeField(Normal):
    def __set__(self, instance, value: datetime.datetime):
        if not isinstance(value, datetime.datetime):
            raise RuntimeError("You should use datetime here")
        instance.values[self.mongo_field] = value.isoformat()

    def __get__(self, instance, owner) -> datetime.datetime:
        value = instance.values.get(self.mongo_field)
        return datetime_parser.parse(value)


class ListField(Reserved):
    def __get__(self, instance, owner):
        class ListFieldModel:
            def __init__(self, model, mongo_field):
                self.model = model
                self.mongo_field = mongo_field

            @property
            def model_field(self) -> list:
                return self.model.values[self.mongo_field]

            def __getitem__(self, item):
                return self.model_field[item]

            def __setitem__(self, key, value):
                self.model_field[key] = value

            def __iter__(self):
                return self.model_field.__iter__()

            def __contains__(self, item):
                return item in self.model_field

            def __len__(self):
                return len(self.model_field)

            async def set_add(self, *args, updated_at=None):
                await self.model.mongo_update({
                    "$addToSet": {self.mongo_field: {
                        '$each': args
                    }},
                    "$set": {
                        "updated_at": get_now().isoformat()
                    }
                }, updated_at=updated_at)
                for e in args:
                    if e not in self.model_field:
                        self.model_field.append(e)

            async def set_push(self, *args, position=0, updated_at=None):
                # 增加指定位置的数组更新，position默认为数组开始
                await self.model.mongo_update({
                    "$push": {self.mongo_field: {
                        '$each': args, "$position":position
                    }},
                    "$set": {
                        "updated_at": get_now().isoformat()
                    }
                }, updated_at=updated_at)
                for e in args:
                    if e not in self.model_field:
                        self.model_field.append(e)


            async def remove(self, *args, updated_at=None):
                await self.model.mongo_update({
                    "$pull": {self.mongo_field: {
                        '$in': args
                    }}
                }, updated_at=updated_at)

                for e in args:
                    self.model_field.remove(e)

        return ListFieldModel(instance, self.mongo_field)
