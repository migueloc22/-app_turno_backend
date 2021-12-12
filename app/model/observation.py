from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String
from config.db import meta,engine
observations = Table("observation",meta,
    Column("id",Integer,primary_key=True),
    Column("observations",String(255)),
    Column("date_creation",DateTime,default= now()),
    Column("state",Boolean,default=True),
    Column("fk_id_turn",ForeignKey("turn.id")),
    Column("fk_id_mechanical_user",ForeignKey("users.id")),
)
meta.create_all(engine)