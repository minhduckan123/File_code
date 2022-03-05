from flask import Flask, render_template, request, url_for, redirect, flash
from quan_ly_truong_hoc import Student, Classroom, ClassList, Subject, Teacher, app, db


@app.route("/")
@app.route("/trang_chu")
def trang_chu():
    return render_template("trang_chu.html", title="Home")


@app.route("/lop_hoc")
def lop_hoc():
    classrooms = Classroom.query.all()
    return render_template("lop_hoc.html", classrooms=classrooms, title="Classroom")

@app.route("/lop_hoc/insert", methods=["POST"])
def insert_lop_hoc():
    if request.method == "POST":
        capacity = request.form["capacity"]

        classroom_insert = Classroom(capacity)
        db.session.add(classroom_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("lop_hoc"))

@app.route("/lop_hoc/update", methods=["GET","POST"])
def update_lop_hoc():
    
    if request.method == "POST":
        edit_classroom = Classroom.query.get(request.form.get("id"))

        edit_classroom.capacity = request.form["capacity"]

        db.session.commit()
    
        flash("Successed!")

        return redirect(url_for("lop_hoc"))
    
@app.route("/lop_hoc/delete/<id>/", methods=["GET", "POST"])
def delete_lop_hoc(id):
    del_classroom = Classroom.query.get(id)
    db.session.delete(del_classroom)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("lop_hoc"))


@app.route("/hoc_sinh")
def hoc_sinh():
    students = Student.query.all()
    return render_template("hoc_sinh.html", students=students, title="Student")

@app.route("/hoc_sinh/insert", methods=["POST"])
def insert_hoc_sinh():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]

        student_insert = Student(firstname, lastname, date_of_birth)
        db.session.add(student_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("hoc_sinh"))

@app.route("/hoc_sinh/update", methods=["GET","POST"])
def update_hoc_sinh():
    
    if request.method == "POST":
        edit_student = Student.query.get(request.form.get("id"))

        edit_student.first_name = request.form["first_name"]
        edit_student.last_name = request.form["last_name"]
        edit_student.date_of_birth = request.form["date_of_birth"]

        db.session.commit()
    
        flash("Successed!")

        return redirect(url_for("hoc_sinh"))
    
@app.route("/hoc_sinh/delete/<id>/", methods=["GET", "POST"])
def delete_hoc_sinh(id):
    del_student = Student.query.get(id)
    db.session.delete(del_student)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("hoc_sinh"))


@app.route("/mon_hoc")
def mon_hoc():
    subjects = Subject.query.all()
    return render_template("mon_hoc.html", subjects=subjects, title="Subject")

@app.route("/mon_hoc/insert", methods=["POST"])
def insert_mon_hoc():
    if request.method == "POST":
        name = request.form["name"]
        capacity = request.form["capacity"]

        subject_insert = Subject(name, capacity)
        db.session.add(subject_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("mon_hoc"))

@app.route("/mon_hoc/update", methods=["GET","POST"])
def update_mon_hoc():
    
    if request.method == "POST":
        edit_subject = Subject.query.get(request.form.get("id"))

        edit_subject.name = request.form["name"]
        edit_subject.capacity = request.form["capacity"]

        db.session.commit()
    
        flash("Successed!")

        return redirect(url_for("mon_hoc"))
    
@app.route("/mon_hoc/delete/<id>/", methods=["GET", "POST"])
def delete_mon_hoc(id):
    del_subject = Subject.query.get(id)
    db.session.delete(del_subject)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("mon_hoc"))
    

@app.route("/giao_vien")
def giao_vien():
    teachers = Teacher.query.all()
    return render_template("giao_vien.html", teachers=teachers, title="Teacher")

@app.route("/giao_vien/insert", methods=["POST"])
def insert_giao_vien():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        subject_taught = request.form["subject_taught"]

        teacher_insert = Teacher(firstname, lastname, subject_taught)
        db.session.add(teacher_insert)
        db.session.commit()

        flash("Successed!")

        return redirect(url_for("giao_vien"))

@app.route("/giao_vien/update", methods=["GET","POST"])
def update_giao_vien():
    
    if request.method == "POST":
        edit_teacher = Teacher.query.get(request.form.get("id"))

        edit_teacher.first_name = request.form["first_name"]
        edit_teacher.last_name = request.form["last_name"]
        edit_teacher.subject_taught = request.form["subject_taught"]

        db.session.commit()
    
        flash("Successed!")

        return redirect(url_for("giao_vien"))
    
@app.route("/giao_vien/delete/<id>/", methods=["GET", "POST"])
def delete_giao_vien(id):
    del_teacher = Teacher.query.get(id)
    db.session.delete(del_teacher)
    db.session.commit()

    flash("Deleted!")

    return redirect(url_for("giao_vien"))
    
if __name__ == "__main__":
    app.run(debug=True)
