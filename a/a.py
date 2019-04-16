from flask import Blueprint, render_template, request, Response, redirect, url_for
from app.exts import sess
from flask import session

blue = Blueprint('a_blue',__name__)

def a_blue(app):
  app.register_blueprint(blueprint=blue)


@blue.route('/home/')
def home():

  # username = request.cookies.get("user")
  username = session.get("user")

  return render_template('home.html', username=username)


@blue.route('/login/',methods=['GET','POST'])
def login():
  if request.method == "GET":
    return render_template('login.html')
  elif request.method == "POST":
    username = request.form.get("username")

    # resp = Response(response="登录成功{}".format(username))
    session["user"] = username
    # resp.set_cookie("user", username)

    # return resp 
    return render_template('main.html',username=username)


@blue.route('/logout/')
def logout():

  # return render_template('login.html')
  # resp = redirect(url_for('a_blue.home'))
  session.pop("user")

  return 'resp'