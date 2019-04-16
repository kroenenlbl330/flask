#!/usr/bin/env python
# -*- coding:utf-8 -
# import redis
from flask import Flask, session
from flask_session import Session as FSession
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
app.debug = True
app.secret_key = 'xxxx'
 
# 设置数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@127.0.0.1:3306/emb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
 
# 实例化SQLAlchemy
db = SQLAlchemy(app)
 
 
 
app.config['SESSION_TYPE'] = 'sqlalchemy'  # session类型为sqlalchemy
app.config['SESSION_SQLALCHEMY'] = db # SQLAlchemy对象
app.config['SESSION_SQLALCHEMY_TABLE'] = 'session' # session要保存的表名称
app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
FSession(app)
 
@app.route('/cdb')
def cdb():
 
    db.create_all()
 
    return 'xx'


@app.route('/index')
def index():
 
    session['k1'] = 'v1'
    session['k2'] = 'v1'
 
    return 'xx'
 
 
if __name__ == '__main__':
    app.run()