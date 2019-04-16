from flask import Blueprint
from app.exts import db
# from app.exts import sess
from flask import session
# from app.models import WaterMeter

blue = Blueprint('first_blue',__name__)

def init_blue(app):
  app.register_blueprint(blueprint=blue)


@blue.route('/')
def index():

  session['k1'] = 'v1'

  return "Hello"

@blue.route('/key/')
def key():


  username = session.get('k1', 'not set')
  print(username)

  return session.get('k1', 'not set')


# # 创建表
# @blue.route('/createdb/')
# def create_db():
#   db.create_all()

#   return "DB Create Success"


# # 删除表
# @blue.route('/dropdb/')
# def drop_db():
#   db.drop_all()

#   return "DB Drop Success"


# # 添加数据
# @blue.route('/adddb/')
# def add_cat():
#   watermeter = WaterMeter()
#   watermeter.meter_code = "S2-14"
#   watermeter.meter_name = "国际交流中心南"
#   watermeter.meter_site ="国际交流中心南"

#   db.session.add(watermeter)
#   db.session.commit()

#   return 'add'


# # 读取数据
# @blue.route('/getdb/')
# def get_cat():
#   cat = Cat()
#   cats = cat.query.all()

#   for a in cats:
#     print(a.name)

#   return 'get'