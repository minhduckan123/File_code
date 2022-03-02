from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "hello_world"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://minhduc@localhost/minhduc"

db = SQLAlchemy(app)

class Classroom(db.Model):
    class_room_id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="classroom", lazy=True)


class Subject(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="subject", lazy=True)

    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"Subject('{self.name}', '{self.capacity}')"


class Teacher(db.Model):
    teacher_id = db.Column(db.Integer, primary_key=True)
    fisrt_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    subject_taught = db.Column(db.String(100), nullable=False)
    classes = db.relationship("Class", backref="teacher", lazy=True)

    def __init__(self,fisrt_name,last_name,subject_taught):
        self.fisrt_name = fisrt_name
        self.last_name = last_name
        self.subject_taught = subject_taught

    def __repr__(self):
        return f"Teacher('{self.fisrt_name}', '{self.last_name}, '{self.subject_taught}')"


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    fisrt_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    classList = db.relationship("ClassList", backref="student", lazy=True)

    def __init__(self,fisrt_name,last_name,date_of_birth):
        self.fisrt_name = fisrt_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"Student('{self.fisrt_name}', '{self.last_name}', '{self.date_of_birth}')"

class ClassList(db.Model):
    class_list_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("Student.student_id"), nullable=False)
    classes = db.relationship("Class")



class Class(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    class_room_id = db.Column(db.Integer, db.ForeignKey("Classroom.class_room_id"), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("Subject.subject_id"), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("Teacher.teacher_id"), nullable=False)
    class_list_id = db.Column(db.Integer, db.ForeignKey("ClassList.class_list_id"), nullable=False)


db.create_all()