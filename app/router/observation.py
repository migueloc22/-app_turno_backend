from fastapi import APIRouter,Response,Depends,HTTPException
from sqlalchemy.sql.expression import select
from config.db import conn
from model.observation import observations
from model.user import users
from schemas.observation import Observation
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
observation = APIRouter()
@observation.get("/observations",response_model=list,tags=["observations"])
def get_turns():
    return conn.execute(observations.select()).fetchall()
@observation.post("/observations",response_model=Observation,tags=["observations"])
def add_turns(observation:Observation):
    new_observation= {
        "observations":observation.observations,
        "fk_id_turn":observation.fk_id_turn,
        "fk_id_mechanical_user":observation.fk_id_mechanical_user,
    }
    query= observations.insert().values(new_observation)
    # print(query)  
    # print(observation)
    # return conn.execute(observations.select()).fetchall()
    result = conn.execute(query)
    return   conn.execute(observations.select().where(observations.c.id == result.lastrowid)).first()
@observation.get("/observations/{id}",tags=["observations"])
def get_turns(id:str):
    query= select(observations.c.id,
            observations.c.observations,
             observations.c.date_creation,
             users.c.name,
            ).select_from(
            observations.join(users,observations.c.fk_id_mechanical_user == users.c.id)
        ).where(observations.c.fk_id_turn==id)
    return conn.execute(query).fetchall()
@observation.delete("/observations/{id}",tags=["observations"])
def delete_turns(id:str):
    query= observations.delete().where(observations.c.id==id)
    print(query)
    result = conn.execute(query)
    # print(observation)
    # return conn.execute(observations.select()).fetchall()
    return Response(status_code=HTTP_204_NO_CONTENT)
@observation.put("/observations",tags=["observations"])
def update_turns(id:str,observation:Observation):
    mod_turn = {"name":observation.name,"email":observation.email,"passworld":observation.passworld}
    query= observations.update().values(mod_turn).where(observations.c.id==id)
    # print(query)
    # print(observation)
    # return conn.execute(observations.select()).fetchall()
    conn.execute(query)
    return Response(status_code=HTTP_204_NO_CONTENT)
