from sanic import Blueprint
from helpers import parse_find_from_request, cursor_result, json_success,assure_user_login
from helpers import mail
from errors import *
from dbconfig import db
import random

notification_blueprint = Blueprint("notification")

@notification_blueprint.post('/find')
async def find(request):
    filter, project, sort, skip, limit = parse_find_from_request(request)
    res = db.notification.find(
        filter=filter,
        projection=project,
        sort=sort,
        skip=skip,
        limit=limit,
    )
    return json_success(list(res))


@notification_blueprint.post('/create')
async def create(request):
    # request.json have sender, receiver, message, is_read, time
    notification = request.json
    notification['_id'] = str(random.randint(100000000, 10000000000))
    db.notification.insert(notification)
    return json_success(None)


@notification_blueprint.post('/<nid>/update')
async def update(request, nid):
    """
    更新字段
    :param request:
    :param nid;
    :return:
    """
    filter = request.json
    res = db.notification.update({"_id": nid}, {"$set": filter})
    return json_success(res)

