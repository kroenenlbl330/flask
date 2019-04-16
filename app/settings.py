import os
import mysql.connector

# 设置template文件路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

def get_db_uri(dbinfo):
  ENGINE = dbinfo.get('ENGINE') or 'sqlite'
  DRIVER = dbinfo.get('DRIVER') or 'pymysql'
  USER = dbinfo.get('USER') or 'root'
  PASSWORD = dbinfo.get('PASSWORD') or 'root'
  HOST = dbinfo.get('HOST') or 'localhost'
  PORT = dbinfo.get('PORT') or '3306'
  NAME = dbinfo.get('NAME') or 'test'

  return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)


# 基类
class Config:
  DEBUG = False
  TESTING = False
  SECRET_KEY = "e@UHOU#!O@#!!OI#P!iepfg"
  SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发者配置环境
class DevelopConfig(Config):
  DEBUG = True

  DATABASE = {
    "ENGINE": "mysql",
    "DRIVER": "mysqlconnector",
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "localhost",
    "PORT": "3306",
    "NAME": "emb"
  }

  # SESSION_TYPE = 'sqlalchemy'
  # SESSION_SQLALCHEMY = db
  # SESSION_SQLALCHEMY_TABLE = 'session' # session要保存的表名称
  # SESSION_PERMANENT = True  # 如果设置为True，则关闭浏览器session就失效。
  # SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
  # SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀  

  SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
  # SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"


# 测试环境
class TestingConfig(Config):
  TESTING = True

  DATABASE = {
    "ENGINE": "mysql",
    "DRIVER": "pymysql",
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "localhost",
    "PORT": "3306",
    "NAME": "DB_name" # 改成测试用的数据库库
  }

  SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 演示环境
class StagingConfig(Config):
  DEBUG = True

  DATABASE = {
    "ENGINE": "mysql",
    "DRIVER": "pymysql",
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "localhost",
    "PORT": "3306",
    "NAME": "DB_name" # 改成演示用的数据库库
  }

  SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


# 线上环境
class ProductConfig(Config):
  DEBUG = True

  DATABASE = {
    "ENGINE": "mysql",
    "DRIVER": "pymysql",
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "localhost",
    "PORT": "3306",
    "NAME": "DB_name" # 改成线上用的数据库库
  }

  SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
  "develop": DevelopConfig,
  "testing": TestingConfig,
  "staging": StagingConfig,
  "product": ProductConfig
}