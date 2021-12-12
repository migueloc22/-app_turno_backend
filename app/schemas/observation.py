from typing import Optional
from pydantic import BaseModel
class Observation(BaseModel):
    id:Optional[str]
    observations: str
    fk_id_turn: str
    fk_id_mechanical_user: str