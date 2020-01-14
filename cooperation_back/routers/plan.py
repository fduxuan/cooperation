from sanic import Blueprint
from helpers import parse_find_from_request, cursor_result, json_success,assure_user_login
from helpers import mail
from errors import *
from dbconfig import db

plan_blueprint = Blueprint("plan")



@plan_blueprint.post('/find')
async def find(request):
    filter, project, sort, skip, limit = parse_find_from_request(request)
    res = db.plan.find(
        filter=filter,
        projection=project,
        sort=sort,
        skip=skip,
        limit=limit,
    )
    return json_success(list(res))


