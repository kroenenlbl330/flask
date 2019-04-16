'''
初始化文件
'''
import os
from flask import Flask

from app.exts import init_exts
from app.views import init_blue
from app.settings import envs

from a.a import a_blue

# with app.app_context():
#     db.init_app(app)

def create_app():
  app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER)
  app.config.from_object(envs.get('develop'))
  app.config['SECRET_KEY'] = os.urandom(24)
  app.config['SESSION_TYPE'] = 'sqlalchemy'  # session类型为sqlalchemy
  app.config['SESSION_SQLALCHEMY'] = db # SQLAlchemy对象
  app.config['SESSION_SQLALCHEMY_TABLE'] = 'session' # session要保存的表名称
  app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
  app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
  app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀


  # 初始化蓝图
  init_blue(app) 
  a_blue(app)

  # 初始化第三方插件、库
  init_exts(app) 



  return app

