# coding=utf-8
import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from flask import logging

class Config_helper(object):

	def __init__(self,name,filenames='db_config.ini'):
		
		conf = ConfigParser.RawConfigParser()
		conf.read(filenames)
		self.host=conf.get(name, 'host')
		self.password=conf.get(name, 'password')
		self.user=conf.get(name, 'user')
		self.database=conf.get(name, 'database')
class Sqlite_config_helper(object):

	def __init__(self,name,filenames='db_config.ini'):
		
		conf = ConfigParser.RawConfigParser()
		conf.read(filenames)
		self.path=conf.get(name, 'path')
		




# load config datebase by MySQL
# mysql=Config_helper('Ncuhome')		
# DB_CONNECT_STRING = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8'%\
# 	(mysql.user,mysql.password,mysql.host,mysql.database)

# # load sqlite 
# sqlite=Sqlite_config_helper('VoteSys')
# DB_CONNECT_STRING='sqlite:///%s'%(sqlite.path)
import sys,os
base_path=os.path.split(os.path.realpath(__file__))[0]
if os.name=='nt':
	DB_CONNECT_STRING='sqlite:///'+base_path+'\\testDB.db'
# DB_CONNECT_STRING='sqlite:///'+base_path+'\\testDB.db'
# print 'getcwd: %s'%os.getcwd()


# if 'engine' in locals() and  globals():
# 	pass
# else:
# 	engine = create_engine(DB_CONNECT_STRING, echo=True)
# 	DB_Session = sessionmaker(bind=engine)
# 	session = DB_Session()
# 	init_db(engine)

# initialize the connection of datebase
engine = create_engine(DB_CONNECT_STRING, echo=True)



from sqlalchemy.ext.declarative import declarative_base 
# base model
BaseModel=declarative_base()
# initialize datebase
def init_db():
    BaseModel.metadata.create_all(engine)
    DB_Session = sessionmaker(bind=engine)
    global session
    session = DB_Session()
    return session

def drop_db():
    BaseModel.metadata.drop_all(engine)

# drop_db()
# init_db()







