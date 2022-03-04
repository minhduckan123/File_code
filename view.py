from flask import Flask, render_template, request, url_for, redirect, flash
from quan_ly_truong_hoc import Student, app, db


@app.route("/")
@app.route("/trang_chu")
def trang_chu():
    return render_template("trang_chu.html", title="Trang chủ")


@app.route("/hoc_sinh")
def hoc_sinh():
    students = Student.query.all()
    return render_template("hoc_sinh.html", students=students, title="Học sinh")

@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        firstname = request.form["first_name"]
        lastname = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]

        student_insert = Student(firstname, lastname, date_of_birth)
        db.session.add(student_insert)
        db.session.commit()

        flash("Success")

        return redirect(url_for("hoc_sinh"))

if __name__ == "__main__":
    app.run(debug=True)
