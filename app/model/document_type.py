from sqlalchemy import Table,Column
from sqlalchemy.sql.operators import ColumnOperators
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine
document_types = Table("document_type",meta,
    Column("id",Integer,primary_key=True),
    Column("name",String(255)),
    Column("alias",String(255))
)
meta.create_all(engine)