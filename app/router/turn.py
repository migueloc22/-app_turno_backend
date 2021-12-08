from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.turn import turns
from schemas.turn import Turn
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
turn = APIRouter()
@turn.get("/turns",response_model=list,tags=["turns"])
def get_turns():
    return conn.execute(turns.select()).fetchall()
# @turn.post("/turns",response_model=Turn,tags=["turns"])
# def add_turns(turn:Turn):
#     new_turn = {"name":turn.name,"email":turn.email,"passworld":turn.passworld}
#     query= turns.insert().values(new_turn)
#     print(query)  
#     # print(turn)
#     # return conn.execute(turns.select()).fetchall()
#     result = conn.execute(query)
#     return   conn.execute(turns.select().where(turns.c.id == result.lastrowid)).first()
# @turn.get("/turns/{id}",tags=["turns"])
# def get_turns(id:str):
#     query= turns.select().where(turns.c.id==id)
#     print(query)
#     # print(turn)
#     # return conn.execute(turns.select()).fetchall()
#     return conn.execute(query).first()
# @turn.delete("/turns/{id}",tags=["turns"])
# def delete_turns(id:str):
#     query= turns.delete().where(turns.c.id==id)
#     print(query)
#     result = conn.execute(query)
#     # print(turn)
#     # return conn.execute(turns.select()).fetchall()
#     return Response(status_code=HTTP_204_NO_CONTENT)
# @turn.put("/turns",tags=["turns"])
# def update_turns(id:str,turn:Turn):
#     mod_turn = {"name":turn.name,"email":turn.email,"passworld":turn.passworld}
#     query= turns.update().values(mod_turn).where(turns.c.id==id)
#     # print(query)
#     # print(turn)
#     # return conn.execute(turns.select()).fetchall()
#     conn.execute(query)
#     return Response(status_code=HTTP_204_NO_CONTENT)
