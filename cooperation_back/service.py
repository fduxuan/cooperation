from sanic import Sanic, response
from sanic.response import text
from sanic_auth import Auth, User
from motor.motor_asyncio import AsyncIOMotorClient
from sanic.response import json as json_response
from mediate import Request
from mediate.errors import MediateError, json_exceptions
from routers import *
from config import Config
from dbconfig import db
from sanic_cors import CORS


config = Config()
app = Sanic()
CORS(app)
session = {}


@app.listener('before_server_start')
async def setups(target_app, _loop):
    """
    服务器未开始前的配置，包括ssl证书配置，mongo数据库连接

    :param target_app: 服务器application对象
    :param _loop: loop，当前asyncio所需的event loop
    :return: None
    """

    # update all config
    # target_app.config.update(config)

    # mongo client
    target_app.mongo_client = AsyncIOMotorClient("mongodb://116.62.46.96")
    # redis pool
    # pool = await aioredis.create_pool(
    #     config.redis,
    #     minsize=5, maxsize=10,
    #     db=config.redis_db,
    #     loop=_loop)
    #
    # target_app.redis = pool


# db stop
@app.listener('after_server_stop')
async def close_db(target_app, _):
    """
    服务停止后清理内容

    :param target_app: 服务器application对象
    :param _: loop，当前asyncio所需的event loop
    :return: None
    """
    target_app.mongo_client.close()
    # graceful shutdown
    # target_app.redis.close()
    # await target_app.redis.wait_closed()


# 异常处理
@app.exception(MediateError)
async def app_error(request, exception):
    """
    用于处理应用级的异常

    :param request: 请求内容
    :param exception: 错误
    :return: 将结果变成json返回
    """
    return json_response(await json_exceptions(request, exception, scope='cornerstone'))


@app.middleware('request')
async def set_session(request):
    """
        设置数据库

        :param request: 请求内容
        :return: None
        """
    # lang = request.headers.get("accept-language", "en_us")
    # lang = request.cookies.get("lang", lang)
    # lang = request.args.get("lang", lang)
    # session = Session(config.session)
    # session_id = request.headers.get("X-Session-ID", None)
    # if session_id is None:
    #     session_id = request.cookies.get("session_id", None)
    # await session.ensure(session_id, timeout=120)
    # request.session = session
    request['session'] = session


# @app.middleware('response')
# async def prevent_xss(request, response):
#     if 'X-Error-Code' not in dict(response.headers):
#         response.headers['X-Error-Code'] = 0
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     response.headers["Access-Control-Allow-Headers"] = "X-Custom-Header,content-type"
#     response.headers['Access-Control-Allow-Methods'] = "POST,GET,OPTIONS"


auth = Auth(app)


@app.post('/api/user/login')
async def profile(request):
    id = request.json['_id']
    name = request.json['nickname']
    user = User(id=id, name=name)
    auth.login_user(request, user)
    return json_success(None)



@app.post('api/user/logout')
@auth.login_required
async def logout(request):
    auth.logout_user(request)
    return json_success(None)





app.blueprint(demand_blueprint, url_prefix="/api/demand")
app.blueprint(user_blueprint, url_prefix="/api/user")
app.blueprint(plan_blueprint, url_prefix="/api/plan")
app.blueprint(notification_blueprint, url_prefix="/api/notification")
app.blueprint(task_blueprint, url_prefix="/api/task")




@app.route('/')
async def hello(request):

    return text("ddd")


if __name__ == '__main__':

    app.run(host="127.0.0.1", debug=True,port=8000)


