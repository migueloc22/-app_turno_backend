from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.user_type import user_types
from schemas.user_type import User_type
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
user_type = APIRouter()
@user_type.get("/user_type_aut",tags=['user_type'])
def get_user_type(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return conn.execute(user_types.select()).fetchall()