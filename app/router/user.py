from fastapi import APIRouter, Response, Depends, HTTPException
from config.db import conn
from model.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
user = APIRouter()


@user.post('/login', tags=["users"])
def login(user: User, Authorize: AuthJWT = Depends()):
    query = users.select().where(users.c.email == user.email)
    usuario = conn.execute(query).first()
    if user.email != usuario.email or user.passworld != usuario.passworld:
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=user.email)    
    conn.execute(users.update().values({"token":access_token}))
    return {"access_token": access_token,"user":usuario}


@user.get("/users", response_model=list, tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users", response_model=User, tags=["users"])
def add_users(user: User):
    new_user = {"name": user.name,
                "email": user.email,
                "passworld": user.passworld,
                "number_document": user.number_document,
                "gender": user.gender,
                "birthday_date": user.birthday_date,
                "fk_id_user_type": 1,
                "fk_id_document_type": user.fk_id_document_type, }
    query = users.insert().values(new_user)
    # print(query)
    # print(user)
    # return conn.execute(users.select()).fetchall()
    result = conn.execute(query)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    # return Response(status_code=HTTP_204_NO_CONTENT)
@user.post("/users_auth", response_model=User, tags=["users"])
def add_users_auth(user: User,Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    new_user = {"name": user.name,
                "email": user.email,
                "passworld": user.passworld,
                "number_document": user.number_document,
                "fk_id_user_type": user.fk_id_user_type,
                "fk_id_document_type": user.fk_id_document_type, }
    query = users.insert().values(new_user)
    # print(query)
    # print(user)
    # return conn.execute(users.select()).fetchall()
    result = conn.execute(query)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}", tags=["users"])
def get_users(id: str):
    query = users.select().where(users.c.id == id)
    # print(query)
    # print(user)
    # return conn.execute(users.select()).fetchall()
    return conn.execute(query).first()


@user.delete("/users/{id}", tags=["users"])
def delete_users(id: str):
    query = users.delete().where(users.c.id == id)
    print(query)
    result = conn.execute(query)
    # print(user)
    # return conn.execute(users.select()).fetchall()
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", tags=["users"])
def update_users(id: str, user: User,Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    mod_user = {"name": user.name,
                "email": user.email,
                "passworld": user.passworld,
                "number_document": user.number_document,
                "fk_id_user_type": user.fk_id_user_type,
                "fk_id_document_type": user.fk_id_document_type, }
    query = users.update().values(mod_user).where(users.c.id == id)
    conn.execute(query)
    return Response(status_code=HTTP_204_NO_CONTENT)
