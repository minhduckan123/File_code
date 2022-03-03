from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "hello_world"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://minhduc@localhost/minhduc"

db = SQLAlchemy(app)

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class")


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class")

    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"Subject('{self.name}', '{self.capacity}')"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    subject_taught = db.Column(db.String(100), nullable=False)
    classes = db.relationship("Class")

    def __init__(self,first_name,last_name,subject_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_taught = subject_taught

    def __repr__(self):
        return f"Teacher('{self.first_name}', '{self.last_name}, '{self.subject_taught}')"


classList = db.Table("classList",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
    db.Column("class_id", db.Integer, db.ForeignKey("class.id"), primary_key=True)
)
    
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_room_id = db.Column(db.Integer, db.ForeignKey("classroom.id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"), nullable=False)
    classList = db.relationship("Student", secondary=classList)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)

    def __init__(self,first_name,last_name,date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"Student('{self.first_name}', '{self.last_name}', '{self.date_of_birth}')"

