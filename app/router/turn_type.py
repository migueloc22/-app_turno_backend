from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.turn_type import turn_types
from schemas.turn_type import Turn_type
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
turn_type = APIRouter()
@turn_type.get("/turn_type_aut",tags=['turn_type'])
def get_turn_type(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return conn.execute(turn_types.select()).fetchall()
@turn_type.get("/turn_type",tags=['turn_type'])
def get_turn_type():
    return conn.execute(turn_types.select()).fetchall()