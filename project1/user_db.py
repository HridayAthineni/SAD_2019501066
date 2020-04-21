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

	def get_user_name(self):
		return self.UserName

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(80), index=False, unique=True, nullable=False)
    title = db.Column(db.String(80), index=True, unique=False, nullable=False)
    author = db.Column(db.String(128))
    year = db.Column(db.Integer, index=False, unique=False, nullable=False)

    def __init__(self, isbn, title, author, year) :
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return self.title