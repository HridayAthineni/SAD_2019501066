import os
import datetime

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from user_db import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
 
@app.route("/")
def index():
    if session.get("name") is not None:
        name = session.get("name") 
        return render_template("home.html", name = name)
    else:
        return redirect("/register")

@app.route("/register", methods = ['POST','GET'])
def signup():
    
    if session.get("name") is not None:
        name = session.get("name") 
        return render_template("home.html", name = name)
    if request.method == 'GET':
        return render_template("Registration.html")
    else:
        name = request.form.get("UserName")
        password = request.form.get("Password")
        email = request.form.get("Email")
        dob = request.form.get("date-of-birth")
        timestamp = datetime.datetime.now()
        user1 = user(name, password, email, dob, timestamp)
        try:
            db.add(user1)
            db.commit()

            msg = "Hello " + name +", Your account was successfully registered"
            return render_template("Registration.html", name = msg)
        except:
            return render_template("Registration.html", name = "User already exists")
@app.route("/admin")
def all_users():
    obj_list = db.query(user).all()
    return render_template("admin.html", obj_list = obj_list)

@app.route("/auth", methods = ['POST',"GET"])
def login():
        if request.method == "GET" and session.get("name") is not None:
            name = session.get("name") 
            return render_template("home.html", name = name)
        elif request.method == "GET":
            msg = "Please login first"
            return render_template("Registration.html", name = msg)
        else:
            name = request.form.get("UserName")
            password = request.form.get("Password")
            session["name"] = name
            user_obj = db.query(user).get(name)
            error_msg = "Please enter valid details"

            if user_obj == None:
                return render_template("Registration.html", name = error_msg)

            elif (name == user_obj.UserName) and (password == user_obj.Password):
                return render_template("home.html", name = name)
            else:
                return render_template("Registration.html", name = error_msg)


@app.route("/logout",methods = ["GET"])
def logout():
    session.clear()
    return redirect("/register")
