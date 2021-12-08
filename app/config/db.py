from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import StaticPool
engine = create_engine('sqlite+pysqlite3:///test.db',connect_args={'check_same_thread': False},poolclass=StaticPool)
meta = MetaData()
conn = engine.connect()
