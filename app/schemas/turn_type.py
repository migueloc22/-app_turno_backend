from typing import Optional
from pydantic import BaseModel
class Turn_type(BaseModel):
    id:Optional[str]
    name:str