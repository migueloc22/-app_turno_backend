from typing import Optional
from pydantic import BaseModel
class Observation(BaseModel):
    id:Optional[str]
    address:str
    observations: str
    date_creation: Optional[str]
    fk_id_turn: str