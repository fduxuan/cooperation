from itertools import count


class MediateError(Exception):

    uni_name = "MEDERR"  # MediateError

    def __init__(self, code, reason=None):
        self.code = code
        self.reason = reason

    @property
    def uuid(self):
        return f"{self.uni_name}:{self.code}"

    def json(self):
        return {
            "type": type(self).__name__,
            "uuid": self.uuid,
            "code": self.code,
            "error": self.reason
        }

    def __call__(self, *, code=None, reason=None):
        return type(self)(code or self.code, reason or self.reason)

    def __str__(self):
        return f'Code: {self.code}, reason: {self.reason}'


async def json_exceptions(request, exception, scope="unknown"):
    """
    return a json response of error

    :param request: sanic request
    :param exception: error
    :param scope: what kind of error
    :return:
    """
    code = getattr(exception, 'code', -1)
    if isinstance(exception, MediateError):
        error = exception.json()
    else:
        error = {
            'code': code,
            'error': str(exception),
            'url': request.url,
            "scope": scope
        }
    if request.content_type == 'application/json':
        error['json'] = str(request.load_json())
    return error


err_count = count()

SUCCESS = MediateError(next(err_count))
UNKNOWN_ERROR = MediateError(next(err_count))
NO_SESSION_LOGIN = MediateError(next(err_count))
NONEXISTENT_MONGO_ID = MediateError(next(err_count))
NO_RECORD = MediateError(next(err_count))
DUPLICATED_MONGO_KEY = MediateError(next(err_count))
MODIFY_OUTDATED_DOCUMENT = MediateError(next(err_count))
INVALID_COMPANY_ID = MediateError(next(err_count))


def find_error(code) -> MediateError:
    for name, obj in globals().items():
        if isinstance(obj, MediateError):
            if obj.code == code:
                return obj
    raise MediateError(code=code)


def update_name():
    for name, obj in globals().copy().items():
        if isinstance(obj, MediateError):
            obj.name = name


update_name()
