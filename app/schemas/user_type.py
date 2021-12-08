from typing import Optional
from pydantic import BaseModel
class User_type(BaseModel):
    id:Optional[str]
    name:str