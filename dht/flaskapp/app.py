from flask import Flask, render_template, request
import sqlite3
import os.path

app = Flask(__name__)
app.secret_key = "tt"
app.config["TEMPLATES_AUTO_RELOAD"] = True

dir_path = os.path.abspath(os.path.dirname("/home/pilloni/"))
db_file = os.path.join(dir_path, "blackberry_dht.db")

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/temp", methods=["GET"])
def temp():
    temp = ""
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        cursor.execute('SELECT * FROM dht WHERE id=1')
        rows = cursor.fetchall()
        temp = str(rows[0][1]) 
    except:
        temp = "none"
    return temp

@app.route("/humidity", methods=["GET"])
def humidity():
    humidity = ""
    try:
        sqliteConnection = sqlite3.connect(db_file)
        cursor = sqliteConnection.cursor()
        cursor.execute('SELECT * FROM dht WHERE id=1')
        rows = cursor.fetchall()
        humidity = str(rows[0][2]) 
    except:
        humidity = "none"
    return humidity




