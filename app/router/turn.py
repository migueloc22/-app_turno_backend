from fastapi import APIRouter,Response,Depends,HTTPException,Request
from sqlalchemy.sql.expression import null, select
from sqlalchemy.orm import aliased
from config.db import conn
from model.turn import turns
from model.user import users
from schemas.turn import Turn
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import exc
turn = APIRouter()
@turn.get("/turns",response_model=list,tags=["turns"])
def get_turns():
    return conn.execute(turns.select()).fetchall()
@turn.post("/turns",response_model=Turn,tags=["turns"])
def add_turns(turn:Turn):
    new_turn = {
        "address":turn.address,
        "number_plate":turn.number_plate,
        "observation":turn.observation,
        "number_turn":turn.number_turn,
        "date":turn.date,
        "hora":turn.hora,
        "fk_id_turn_type":turn.fk_id_turn_type,
        "fk_id_turn_state":1,
        "fk_id_client_user":turn.fk_id_client_user,
        "fk_id_mechanical_user":turn.fk_id_mechanical_user,
    }
    query= turns.insert().values(new_turn)
    # print(query)  
    # print(turn)
    # return conn.execute(turns.select()).fetchall()
    result = conn.execute(query)
    return   conn.execute(turns.select().where(turns.c.id == result.lastrowid)).first()
@turn.get("/turns/{id}",tags=["turns"])
def get_turns(id:str):
    user_client = aliased(users)
    user_mechanical = aliased(users)
    query= select(turns.c.id,
             turns.c.date,
              turns.c.hora,
              (user_mechanical.c.name).label('name_mechanical'),
              (user_client.c.name).label('name_client'),
              turns.c.observation,
              turns.c.number_plate,
              turns.c.fk_id_turn_state,
              ).select_from(
                turns.join(user_mechanical,turns.c.fk_id_mechanical_user == user_mechanical.c.id)
                .join(user_client,turns.c.fk_id_client_user == user_client.c.id)
            ).where(turns.c.id==id)
    #print(query)
    # print(turn)
    # return conn.execute(turns.select()).fetchall()
    return conn.execute(query).first()
@turn.get("/turns_list/{id}/{date}",tags=["turns"])
def get_turns_list(id:str,date:str):
    try:
        query= select(turns.c.id, turns.c.date, turns.c.hora,users.c.name).select_from(
            turns.join(users,turns.c.fk_id_mechanical_user == users.c.id)
        ).where(turns.c.fk_id_client_user==id,turns.c.date==date)
        # for row in conn.execute(query).fetchall():
        #     print(row)
        return conn.execute(query).fetchall()
    except exc.SQLAlchemyError as e:
        print(type(e))
        return type(e)
@turn.get("/turns_agenda/{id}/{date}",tags=["turns"])
def get_turns_agenda(id:str,date:str):
    try:
        query= select(turns.c.id, turns.c.date, turns.c.hora,users.c.name,).select_from(
            turns.join(users,turns.c.fk_id_mechanical_user == users.c.id)
        ).where(turns.c.fk_id_mechanical_user==id,turns.c.date==date)
        # for row in conn.execute(query).fetchall():
        #     print(row)
        return conn.execute(query).fetchall()
    except exc.SQLAlchemyError as e:
        print(type(e))
        return type(e)
@turn.delete("/turns/{id}",tags=["turns"])
def delete_turns(id:str):
    query= turns.delete().where(turns.c.id==id)
    # print(query)
    result = conn.execute(query)
    # print(turn)
    # return conn.execute(turns.select()).fetchall()
    return Response(status_code=HTTP_204_NO_CONTENT)
@turn.put("/turns",tags=["turns"])
def update_turns(id:str,turn:Turn):
    mod_turn = {"name":turn.name,"email":turn.email,"passworld":turn.passworld}
    query= turns.update().values(mod_turn).where(turns.c.id==id)
    # print(query)
    # print(turn)
    # return conn.execute(turns.select()).fetchall()
    conn.execute(query)
    return Response(status_code=HTTP_204_NO_CONTENT)
@turn.put("/turns_states/{id}/{status}",tags=["turns"])
def update_turns_states(id:str,status:str):
    mod_turn = {"fk_id_turn_state":status}
    query= turns.update().values(mod_turn).where(turns.c.id==id)
    # print(query)
    # print(turn)
    # return conn.execute(turns.select()).fetchall()
    conn.execute(query)
    return Response(status_code=HTTP_204_NO_CONTENT)
