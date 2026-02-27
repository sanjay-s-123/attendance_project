from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="mysql-15630cd5-ssanjay12022008-d8a3.j.aivencloud.com",
    user="avnadmin",
    password="AVNS_pw9-theoTtgDmFaK8iS",
    database="defaultdb"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def splash():
    return render_template("splash.html")
@app.route('/home')
def login():
    return render_template("home.html")

@app.route('/login', methods=['POST'])
def check_login():
    email = request.form['email'].strip()
    password = request.form['password'].strip()

    cursor.execute("SELECT * FROM students WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        if user['password'] == password:
            return "Login Successful"
        else:
            return render_template("home.html", popup="Wrong Password")
    else:
        return render_template("home.html", popup="Wrong email id")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
