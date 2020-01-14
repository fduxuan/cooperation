from .meta import ModelMeta


def within_set(fields: set, *args: [dict]):
    for data in args:
        for key, value in data.items():
            if key in fields:
                yield key, value


def not_in_set(fields: set, *args: [dict]):
    for data in args:
        for key, value in data.items():
            if key not in fields:
                yield key, value


class BaseModel:
    """
    基础Model，负责内存和权限的判断，和数据库读写无关
    """
    has_extra = False
    Meta = ModelMeta

    reserved_fields: set = None
    normal_fields: set = None

    def __init__(self):
        self.values = dict()
        if not hasattr(self, 'reserved_fields'):
            self.reserved_fields = set()
        if not hasattr(self, 'normal_fields'):
            self.normal_fields = set()
        self.fields = self.reserved_fields.copy().union(self.normal_fields)

    def update_reserved_values(self, data=None, **kwargs):
        for key, value in within_set(self.reserved_fields, data, kwargs):
            self.values[key] = value

    def update_normal_values(self, data=None, **kwargs):
        for key, value in within_set(self.normal_fields, data, kwargs):
            self.values[key] = value

    def update_extra_values(self, data=None, to_raise=False, **kwargs):
        if not self.has_extra:
            if to_raise:
                raise RuntimeError("Extra Fields are not allowed")
            return
        for key, value in not_in_set(self.fields, data, kwargs):
            self.values[key] = value

    def copy(self):
        result = type(self)()
        result.reserved_fields = self.reserved_fields.copy()
        result.normal_values = self.normal_fields.copy()
        result.reserved_values = self.values.copy()

    def clear(self):
        self.values.clear()

    # container behaviors
    def get(self, key, default=None):
        return self.values.get(key, default)

    def __contains__(self, item):
        return self.values.__contains__(item)

    def __getitem__(self, item):
        return self.values.__getitem__(item)

    def __iter__(self):
        return self.values.__iter__()
