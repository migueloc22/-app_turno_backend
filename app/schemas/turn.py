from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta
class Turn(BaseModel):
    id:Optional[str]
    address:str
    number_plate:str
    observation:str
    number_turn:Optional[str]
    date:Optional[date]
    hora:Optional[time]
    state:Optional[str]
    fk_id_turn_state:Optional[str]
    fk_id_turn_type:str
    fk_id_client_user:str
    fk_id_mechanical_user:str