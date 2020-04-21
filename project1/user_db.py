from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
	
	__tablename__ = "users"
	UserName = db.Column(db.String, primary_key = True)
	Password = db.Column(db.String, nullable = False)
	Email = db.Column(db.String, nullable = False)
	date_of_birth = db.Column(db.String, nullable = False)
	timestamp = db.Column(db.DateTime, nullable = False)
		
	def __init__(self, UserName, Password, Email, date_of_birth, timestamp):
		self.UserName = UserName
		self.Password = Password
		self.Email = Email
		self.date_of_birth = date_of_birth
		self.timestamp = timestamp