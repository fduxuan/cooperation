from mediate.config import DefaultConfig, ConfigItem


class Config(DefaultConfig):
    n_workers = ConfigItem("WORKERS", default=1, cast=int)
