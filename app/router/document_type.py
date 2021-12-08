from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.document_type import document_types
from schemas.document_type import Document_type
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
document_type = APIRouter()
@document_type.get("/document_type",tags=['document_type'])
def get_document_type():
    return conn.execute(document_types.select()).fetchall()
@document_type.get("/document_type_aut",tags=['document_type'])
def get_document_type(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return conn.execute(document_types.select()).fetchall()