from sanic import Blueprint
from helpers import parse_find_from_request, cursor_result, json_success
from model import Demo
from dbconfig import db



demand_blueprint = Blueprint("demand")


@demand_blueprint.get('/show')
async def show(request):
    # query, project, sort = parse_find_from_request(request)
    # return Demo(mydb).find(
    #     query=query,
    #     project=project,
    #     sort=sort,
    #     prune=True
    # )
    p = db.info.find_one()
    print(p)
    return json_success(p)


@demand_blueprint.get('/find')
async def find(request):

    p = list(db.info.find())

    return json_success(p)