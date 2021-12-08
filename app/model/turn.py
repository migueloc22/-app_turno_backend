from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime, Integer, String
from config.db import meta,engine
turns = Table("turn",meta,
    Column("id",Integer,primary_key=True),
    Column("address",String(255)),
    Column("number_plate",String(255)),
    Column("number_turn",Integer,nullable=true),
    Column("date_creation",DateTime,default= now()),
    Column("date",Date,nullable=true),
    Column("hora",Date,nullable=true),
    Column("state",Boolean,default=True),
    Column("fk_id_turn_type",ForeignKey("turn_type.id")),
    Column("fk_id_turn_state",ForeignKey("turn_state.id")),
    Column("fk_id_client_user",ForeignKey("users.id")),
    Column("fk_id_mechanical_user",ForeignKey("users.id")),
)
meta.create_all(engine)