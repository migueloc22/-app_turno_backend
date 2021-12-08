from typing import Optional
from pydantic import BaseModel
class Turn(BaseModel):
    id:Optional[str]
    address:str
    number_plate:str
    number_turn:Optional[str]
    date_creation:str
    date:Optional[str]
    hora:Optional[str]
    fk_id_turn_type:str
    fk_id_client_user:str
    fk_id_client_user:str