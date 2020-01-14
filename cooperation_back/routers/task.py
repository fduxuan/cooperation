from sanic import Blueprint
from helpers import parse_find_from_request, cursor_result, json_success,assure_user_login
from helpers import mail
from errors import *
from dbconfig import db
import random

task_blueprint = Blueprint("task")

@task_blueprint.post('/create')
async def create(request):
    session = request['session']
    uid_1 = session['_auth']['uid']
    pid = request.json['pid']
    plan = db.plan.find_one({"_id": pid})
    task = db.task.find({"pid": pid, "$or": [{'uid1': uid_1}, {'uid2': uid_1}]})

    if task != None:
        raise TASK_ALREADY_USE(reason="宁已经有此任务！")
    plan['pid'] = pid
    plan['start'] = request.json['start']
    plan['uid1'] = uid_1
    plan['uid2'] = request.json['uid']
    plan['score'] ={'uid1': 0, 'uid2': 0}
    plan["_id"] = str(random.randint(100000000, 10000000000))
    plan['state'] = 'todo'
    plan['finish'] = {'uid1': [0]*int(plan['days']), 'uid2':[0]*int(plan['days'])}
    db.task.insert(plan)
    return json_success(plan)


@task_blueprint.post('/find')
async def find(request):
    filter, project, sort, skip, limit = parse_find_from_request(request)
    res = db.task.find(
        filter=filter,
        projection=project,
        sort=sort,
        skip=skip,
        limit=limit,
    )
    return json_success(list(res))


@task_blueprint.post('/<tid>/update')
async def update(request, tid):
    """
    更新字段
    :param request:
    :param uid;
    :return:
    """
    filter = request.json
    res = db.task.update({"_id": tid}, {"$set": filter})
    return json_success(res)
