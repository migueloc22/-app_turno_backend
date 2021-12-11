from sqlalchemy import Table,Column,ForeignKey
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import Date, Integer, String
from config.db import meta,engine
users = Table("users",meta,
    Column("id",Integer,primary_key=True),
    Column("name",String(255)),
    Column("email",String(255),unique=True),
    Column("passworld",String(255)),
    Column("number_document",String(12)),
    Column("gender",String(12)),
    Column("birthday_date",Date,nullable=true),
    Column('fk_id_user_type',ForeignKey('user_type.id')),
    Column('fk_id_document_type',ForeignKey('document_type.id')),
    Column("token",String(500),unique=True,nullable=True),
    )
meta.create_all(engine)