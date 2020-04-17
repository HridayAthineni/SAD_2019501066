from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
	
	__tablename__ = "users"
	UserName = db.Column(db.String, primary_key = True)
	Password = db.Column(db.String, nullable = False)
	Email = db.Column(db.String, nullable = False)
	gender = db.Column(db.String, nullable = False)
	date_of_birth = db.Column(db.String, nullable = False)
		
	def __init__(self, UserName, Password, Email, gender, date_of_birth):
		self.UserName = UserName
		self.Password = Password
		self.Email = Email
		self.gender = gender
		self.date_of_birth = date_of_birth