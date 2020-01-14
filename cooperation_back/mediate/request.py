from aioredis.pool import ConnectionsPool
from sanic.exceptions import abort
from sanic.request import Request as _Request


from .i18n import I18N


class Request(_Request):

    drop_user = None
    meta = None
    demo = None
    i18n: I18N
    db = None

    @property
    def mime(self):
        """
        计算mime类型

        :return:
        """
        content_type = self.content_type
        mime_type = content_type.split(';')[0]
        mime_type = mime_type.strip()
        return mime_type

    @property
    def json(self):
        """
        安全地返回json

        :return:
        """
        if self.method == 'POST' and self.mime != 'application/json':
            abort(406)
        return super().json

    @property
    def unsafe_json(self):
        return super().json

    @property
    def redis(self) -> ConnectionsPool:
        return self.app.redis
