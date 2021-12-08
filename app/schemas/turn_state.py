from typing import Optional
from pydantic import BaseModel
class Turn_state(BaseModel):
    id:Optional[str]
    name:str