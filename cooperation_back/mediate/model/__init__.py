from json import dumps as _dumps

from .model import Model, Cursor
from .field import *


def jsonify_special(obj):
    if isinstance(obj, Model):
        return obj.values
    if isinstance(obj, datetime.datetime):
        if obj.tzinfo is None:
            obj = obj.replace(tzinfo=datetime.timezone.utc)
        return obj.isoformat()
    raise TypeError(f"无法序列号对象{type(obj)}")


def jsonify(obj):
    return _dumps(obj, default=jsonify_special)
