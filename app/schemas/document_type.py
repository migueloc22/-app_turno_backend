from typing import Optional
from pydantic import BaseModel
class Document_type(BaseModel):
    id:Optional[str]
    name:str
    alias:str