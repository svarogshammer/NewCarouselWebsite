from flask import Flask, redirect, url_for, render_template, request
from assignment_manager import AssignmentManager
from werkzeug.utils import secure_filename

import mysql.connector
import json

app = Flask(__name__)


@app.route("/about.html")
def about():
    db = mysql.connector.connect(host='database-1.c18goo9xcwlq.us-east-1.rds.amazonaws.com', user='admin',
                                    password='12349876', db="database-1")
    #db = mysql.connector.connect(host='instance1.cyrozt6t970f.us-east-1.rds.amazonaws.com', user='admin',
    #                             password='12349876', db="assignments")

    cursor = db.cursor()
    sql_query = """SELECT * FROM database-1"""
    cursor.execute(sql_query)
    data = cursor.fetchall()

    db.commit()

    return render_template("Landing2.html", content=data)
    #return render_template("index4.html", content=data)
    

@app.route("/deanstest")
def test():
    db = mysql.connector.connect(host='database-1.c18goo9xcwlq.us-east-1.rds.amazonaws.com', user='admin',
                                    password='12349876', db="database-1")
    #db = mysql.connector.connect(host='instance1.cyrozt6t970f.us-east-1.rds.amazonaws.com', user='admin',
    #                            password='12349876', db="assignments")

    cursor = db.cursor()
    #database-1
    sql_query = """SELECT * FROM database-1"""
    #sql_query = """SELECT * FROM Assignments"""
    cursor.execute(sql_query)
    data = cursor.fetchall()
    db.commit()

    # cursor.execute("DELETE from Assignments")
    return render_template("Landing2.html", content=data)


@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

        assignment_manager = AssignmentManager()
        assignment_manager.test(f.filename)

        return f.filename


if __name__ == "__main__":
    app.run()
