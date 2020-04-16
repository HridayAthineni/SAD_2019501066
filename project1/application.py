import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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
    return "TODO"

@app.route("/register", methods = ['POST','GET'])
def signup():
	if request.method == 'GET':
		return render_template("Registration.html")
	else:
		name = request.form.get("UserName")
		msg = "Hello " + name +", Your account was successfully registered"
	return render_template("Registration.html", name = msg)