from flask import Flask, redirect, render_template, url_for, request
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config["MYSQL HOST"] = "localhost"
app.config["MYSQL_USER"] = "minhduc"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "minhduc"


mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("test.html")


@app.route("/test", methods=["POST"])
def test():
    name = request.form["name"]
    sex = request.form["sex"]
    age = request.form["age"]
    class_ = request.form["class"]

    cursor = mysql.connection.cursor()

    cursor.execute(f"INSERT INTO hoc_sinh (name, sex, age, class) VALUES (%s, %s, %s, %s)",(name, sex, age, class_))
    mysql.connection.commit()
    cursor.close()
    return "Done!"

app.run(debug=True)