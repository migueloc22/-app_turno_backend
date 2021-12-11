from sqlalchemy import create_engine, MetaData
from sqlalchemy.pool import StaticPool
# sqlite
# engine = create_engine('sqlite+pysqlite3:///test.db',connect_args={'check_same_thread': False},poolclass=StaticPool)
# mysql
engine = create_engine("mysql+pymysql://root@localhost:3306/app_turn",encoding="utf-8",echo=True)
meta = MetaData()
conn = engine.connect()
