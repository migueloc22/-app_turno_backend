from fastapi import APIRouter,Response,Depends,HTTPException
from config.db import conn
from model.turn_state import turn_states
from schemas.turn_state import Turn_state
from starlette.status import HTTP_204_NO_CONTENT
from fastapi_jwt_auth import AuthJWT
turn_state = APIRouter()
@turn_state.get("/turn_state_aut",tags=['turn_state'])
def get_turn_state(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return conn.execute(turn_states.select()).fetchall()