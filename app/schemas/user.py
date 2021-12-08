from typing import Optional
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer
class User(BaseModel):
    id:Optional[str]
    name:str
    email:str
    passworld:str
    number_document:str
    fk_id_user_type:Optional[str]
    fk_id_document_type:str
    # token:str