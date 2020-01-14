from functools import wraps as _wraps

from sanic import response as _response
from mediate.model import jsonify, Cursor
from errors import *
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random

def json_success(target=None):
    """
    返回成功的json结果

    :param target
    :return:
    """
    return _response.json({'code': 0, 'data': target}, dumps=jsonify)


def parse_find_from_request(request):
    """
    parse query project and sort from request
    :param request:
    :return:
    """
    json = request.json or dict()
    query = json.get('filter', dict())
    project = json.get('project', None)
    sort = json.get('sort', None)
    skip = json.get('skip', 0)
    limit = json.get('limit', 0)
    if sort is None:
        sort = [("created_at", 1)]
    if isinstance(sort, dict):
        sort = [(key, value) for key, value in sort.items()]
    return query, project, sort, skip, limit


def stream_cursor(cursor, count=0, content_type='application/json'):
    """
    调用sanic的stream功能把一个cursor里的内容发送到前端

    :param cursor:
    :param count:
    :param content_type:
    :return:
    """
    async def streaming(response):
        """

        :param response:
        :return:
        """
        await response.write(b'{"code": 0, "data": [')
        started = False
        async for one in cursor:
            if started:
                await response.write(b',')
            else:
                started = True
            buffer = jsonify(one)
            await response.write(buffer.encode())
        await response.write(b'], "count": %d}' % count)
    return _response.stream(streaming, content_type=content_type)


def cursor_result(
        limit_default, skip_default=0, limit_max=None
):
    """
    返回一个cursor，并自动获取skip和limit，以及决定是否是count结果

    :param limit_default: None for inf
    :param skip_default:
    :param limit_max: None for inf
    :return:
    """
    def real_decorator(handler):
        """

        :param handler:
        :return:
        """
        @_wraps(handler)
        async def cursor_result_handler(request, *args, **kwargs):
            """

            :param request:
            :param args:
            :param kwargs:
            :return:
            """
            cursor: Cursor = await handler(request, *args, **kwargs)
            is_count = int(request.args.get('count', 0))
            if is_count:
                return json_success(await cursor.count())

            json = request.json or {}
            limit = json.get('limit', limit_default)
            if limit is not None:
                if limit_max is not None:
                    limit = min(limit, limit_max)
                limit = max(limit, 0)

            skip = json.get('skip', skip_default)
            skip = max(skip, 0)

            count = await cursor.count()
            cursor.limit(limit)
            cursor.skip(skip)
            if json.get('count', False):
                return json_success(count)
            return stream_cursor(cursor, count=count)

        return cursor_result_handler
    return real_decorator


def build_company_user_id_from_request(request, uid):
    """
    从request里的company id和user id生成一个唯一的身份与之对应

    :param request: sanic的request
    :param uid: user id
    :return: 生成的company user id
    """
    return f"droproblem.{request.company['_id']}.{uid}"


def assure_user_login(handler):
    @_wraps(handler)
    async def ensure_user_r_handler(request, *args, **kwargs):
        user = request['session']
        if user == {}:
            raise UNBOUND_USER(reason="宁没有登录")
        return await handler(request, *args, **kwargs)
    return ensure_user_r_handler







def mail(receiver):
    # 发件人邮箱账号
    my_sender = 'fang@droproblem.com'
    # user登录邮箱的用户名，password登录邮箱的密码（授权码，即客户端密码，非网页版登录密码），但用腾讯邮箱的登录密码也能登录成功
    my_pass = '980923FXJfzdHL,.'
    # 收件人邮箱账号
    my_user = receiver['email']
    ret = True
    check = random.randint(1000, 10000)
    message = "欢迎使用cornerstone!\n 您的邮箱验证码为："+str(check)
    try:
        # 邮件内容
        msg = MIMEText(message, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["cornerstone", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr([receiver['nickname'], my_user])
        # 邮件的主题
        msg['Subject'] = "cornerstone邮箱验证"

        # SMTP服务器，腾讯企业邮箱端口是465，腾讯邮箱支持SSL(不强制)， 不支持TLS
        # qq邮箱smtp服务器地址:smtp.qq.com,端口号：456
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        # 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = str(check)
    except Exception:
        ret = False
    return ret


