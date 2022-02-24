from flask import Flask, redirect, render_template, url_for, request
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config["MYSQL HOST"] = "localhost"
app.config["MYSQL_USER"] = "minhduc"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "minhduc"


mysql = MySQL(app)

cursor = mysql.connection

# mysql.connection.commit()


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home", methods= ["POST"])
def home():
   username = request.form["username"]

   if username == "duc":
      return render_template("home_admin.html")
   else:
      return render_template("home_user.html")

@app.route("/home/user", methods=["POST"])
def user():
   if request.form["table"] == "create_table":
      return "1"
   elif request.form["table"] == "update_table":
      return "2"
   elif request.form["table"] == "read_table":
      return "3"
   elif request.form["table"] == "delete_table":
      return "4"
      

if __name__ == '__main__':
   app.run(debug = True)