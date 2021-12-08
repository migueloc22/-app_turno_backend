from sqlalchemy import Table,Column
from sqlalchemy.sql.operators import ColumnOperators
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine
user_types = Table("user_type",meta,
    Column("id",Integer,primary_key=True),
    Column("name",String(255))
)
meta.create_all(engine)