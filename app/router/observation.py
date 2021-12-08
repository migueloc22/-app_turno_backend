from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.observation import observations
from schemas.observation import Observation
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
observation = APIRouter()
@observation.get("/observations",response_model=list,tags=["observations"])
def get_turns():
    return conn.execute(observations.select()).fetchall()
# @observation.post("/observations",response_model=Observation,tags=["observations"])
# def add_turns(observation:Observation):
#     new_turn = {"name":observation.name,"email":observation.email,"passworld":observation.passworld}
#     query= observations.insert().values(new_turn)
#     print(query)  
#     # print(observation)
#     # return conn.execute(observations.select()).fetchall()
#     result = conn.execute(query)
#     return   conn.execute(observations.select().where(observations.c.id == result.lastrowid)).first()
# @observation.get("/observations/{id}",tags=["observations"])
# def get_turns(id:str):
#     query= observations.select().where(observations.c.id==id)
#     print(query)
#     # print(observation)
#     # return conn.execute(observations.select()).fetchall()
#     return conn.execute(query).first()
# @observation.delete("/observations/{id}",tags=["observations"])
# def delete_turns(id:str):
#     query= observations.delete().where(observations.c.id==id)
#     print(query)
#     result = conn.execute(query)
#     # print(observation)
#     # return conn.execute(observations.select()).fetchall()
#     return Response(status_code=HTTP_204_NO_CONTENT)
# @observation.put("/observations",tags=["observations"])
# def update_turns(id:str,observation:Observation):
#     mod_turn = {"name":observation.name,"email":observation.email,"passworld":observation.passworld}
#     query= observations.update().values(mod_turn).where(observations.c.id==id)
#     # print(query)
#     # print(observation)
#     # return conn.execute(observations.select()).fetchall()
#     conn.execute(query)
#     return Response(status_code=HTTP_204_NO_CONTENT)
