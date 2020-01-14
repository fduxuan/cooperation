import base64 as _base64
import datetime as _datetime
import os as _os
import urllib.parse as _url_parser

import dateutil.parser as _date_parser


def get_module_path():
    """
    get the path of taskalive package

    :return:
    """
    module_path = getattr(get_module_path, 'module_path', None)
    if module_path is not None:
        return module_path
    script_path = _os.path.realpath(__file__)
    script_dir = _os.path.dirname(script_path)
    module_path = _os.path.realpath(_os.path.join(script_dir, _os.pardir))
    setattr(get_module_path, 'module_path', module_path)
    return module_path


def get_now():
    return _datetime.datetime.now(_datetime.timezone.utc)


def parses_iso_date(iso_date_str: str):
    return _date_parser.parse(iso_date_str)


def get_uuid():
    bs = str(_datetime.datetime.now()).encode()
    bs += _os.urandom(32)
    return _base64.urlsafe_b64encode(bs).decode().replace("=", "")


def encode_url_component(string):
    return _url_parser.quote(string)
