# coding=utf-8
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.types import CHAR, Integer, String,DateTime, TIMESTAMP,Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import sessionmaker,relationship, backref
import connection

# based model 
# every subclass need has a table in datebase
Base = connection.BaseModel

# the sqlite doesn't forse the lenth of varchar
class Article(Base):
	__tablename__='article'
	id = Column(Integer,autoincrement=True, primary_key=True)
	art_url=Column(String(200),nullable=False)
	art_type=Column(String(50))
	content=Column(String(10000))
	is_send=Column(Boolean)
	insert_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

