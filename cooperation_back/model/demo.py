import datetime
from mediate.model import Model, ListField, Normal, DateTimeField, Reserved
from mediate.helpers import get_now


class Demo(Model, metaclass=Model.Meta):
    coll_name = 'info'
    name = Normal