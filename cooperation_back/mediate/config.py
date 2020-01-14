import os
from typing import Any


class _Required:
    pass


def get_value_from_env(name, default, cast):
    value = os.environ.get(name, default)
    if value is _Required:
        raise RuntimeError(f"Config {name} from environment is required.")
    value = cast(value)
    return value


class ConfigItem:
    """
    Environ 用于指定如何从环境变量中获取配置信息
    """

    def __init__(self, name: str, default: Any = _Required, cast=lambda x: x):
        self.name = name
        self.default = default
        self.cast = cast

    def get(self):
        return get_value_from_env(self.name, self.default, self.cast)


class Config:
    """
    创建一个Config，当进行初始化当时候，会对所有的ConfigItem类型的变量从环境变量中加载
    """
    Item = ConfigItem

    def __init__(self):
        self.dict = dict()
        self.values = dict()
        names = dir(self)
        for one in names:
            value = getattr(self, one)
            if isinstance(value, ConfigItem):
                value = value.get()
                setattr(self, one, value)
                self.values[one] = value

    def __iter__(self):
        return iter(self.values.items())


class DefaultConfig(Config):
    """
    默认的一些设置
    """
    mongo_url = Config.Item("MONGO_URL", default="mongodb://116.62.46.96")
    redis = Config.Item("REDIS", default="redis://localhost")
    redis_db = Config.Item("REDIS_DB", default=0, cast=int)
    addr = Config.Item("ADDR", default="localhost:8080")
    prefix = Config.Item("PREFIX", default="")
    session = Config.Item("SESSION", default="http://localhost:1234")
    lang = Config.Item("LANG", default="en_US")
    debug = Config.Item("DEBUG", default=True, cast=lambda x: bool(int(x)))
