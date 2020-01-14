from sanic import Blueprint
from helpers import parse_find_from_request, cursor_result, json_success,assure_user_login
from helpers import mail
from errors import *
from dbconfig import db
import requests



user_blueprint = Blueprint("user")


@user_blueprint.post('/auth')
async def auth(request):
    """
    :param request:
    :return:
    """
    access_token = request.json['access_token']
    QQ_APP_ID = '101834891'
    userId = request.json['userId']
    url = "https://graph.qq.com/user/get_user_info?access_token=" + access_token + "&oauth_consumer_key=" + QQ_APP_ID + "&openid=" + userId;
    p = requests.get(url)

    return json_success(p.json())



@user_blueprint.post('/register')
async def register(request):
    """
    提交参数应为：{name: xxx, sex:xxx, desc:xxxx}
    :param reqeust:
    :param qq号
    :return:
    """

    query = {"email": request.json['email']}
    user = db.user.find_one(filter=query)
    if user is not None:
        raise ALLREADY_REGISTER_USER(reason="该邮箱已被注册！")
    insert_data = request.json
    insert_data['_id'] = request.json['email']
    res = db.user.insert(insert_data)
    return json_success(res)


@user_blueprint.post('/find')
async def find(request):
    filter, project, sort, skip, limit = parse_find_from_request(request)
    res = db.user.find(
        filter=filter,
        projection=project,
        sort=sort,
        skip=skip,
        limit=limit,
    )
    return json_success(list(res))


@user_blueprint.post('/<uid>/update')
async def update(request, uid):
    """
    更新字段
    :param request:
    :param uid;
    :return:
    """
    filter = request.json
    res = db.user.update({"_id": uid}, {"$set": filter})
    return json_success(res)


@user_blueprint.get('/<uid>/show')
async def show(request, uid):
    res = db.user.find_one({"_id": uid})
    if res is None:
        raise UNBOUND_USER
    return json_success(res)


@user_blueprint.get('/info')
@assure_user_login
async def info(request):
    session = request['session']

    _id = session['_auth']['uid']
    user = db.user.find_one({"_id": _id})
    return json_success(user)


@user_blueprint.post('/email')
async def email(request):
    receiver = {}

    receiver['email'] = request.json['email']
    receiver['nickname'] = request.json['nickname']
    ret = mail(receiver)

    return json_success(ret)


@user_blueprint.post('/add/friend')
@assure_user_login
async def add_friend(request):
    uid = request.json['uid']
    session = request['session']
    _id = session['_auth']['uid']
    user = db.user.find_one({"_id": _id})
    friend = user.get('friend', [])
    if uid not in friend:
        friend.append(uid)
    else :
        raise MUTIPLE_FRIEND(reason="请勿重复添加！")
    user['friend'] = friend
    res = db.user.update({"_id": _id}, user)
    return json_success(res)

