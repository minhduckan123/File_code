from flask import Flask, render_template
from quan_ly_truong_hoc import Student, app


@app.route("/")
@app.route("/trang_chu")
def trang_chu():
    return render_template("trang_chu.html")

@app.route("/hoc_sinh")
def hoc_sinh():
    students = Student.query.all()
    return render_template("hoc_sinh.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)