import os
import datetime

from flask import Flask, render_template, redirect, request, session
from sqlalchemy import create_engine
from flask_session import Session
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import jsonify


from voters_db import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://kkyorsvsudekje:50d2cf9cd8cf7d0e44f2e39c3de05d71bedc0abb959a876e0824917f71a25ab7@ec2-54-162-119-125.compute-1.amazonaws.com:5432/dc7hua40a4apb6"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config.from_object(__name__)
Session(app)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/add", methods=["GET", "POST"])
def add_voter():
    if request.method == "POST":
        userid = request.form.get("UserId")
        password = request.form.get("Password")
        age = request.form.get("Age")
        area = request.form.get("Area")
        vote = voter(userid, password, age, area, False)
        # try:
        user = db.session.query(voter).get(userid)
        ageVerify = db.session.query(voter).get(age)
        # try:
        if not user:
            db.session.add(vote)
            print("added")
            db.session.commit()
            print("commited")
            return render_template("home.html", name="Your registration is successful")
        else:
            return render_template("home.html", name="User already exists or Age restricted")

        # except:
        #     # print(Exception)
        #     return render_template("home.html", name="Give correct details")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def log():
    # print("hello from login")
    if request.method == "POST":
        print("hello from POST111111111111111111")
        name = request.form.get("UserId")
        password = request.form.get("Password")
        user = db.session.query(voter).get(name)
        if user:
            pw = user.Password
            if voter.query.get(name).status is False:
                if request.form.get("UserId") == "admin" and password == pw:
                    data = db.session.query(candidate)
                    print(data, "#####################################")
                    return render_template("login.html", data=data)
                elif(user.UserId == name and password == pw):
                    data = db.session.query(candidate)
                    session['id'] = name
                    return render_template("candidates.html", data=data)
            else:
                return render_template("home.html", name="Already Voted")
        else:
            return render_template("home.html", name="You are not registered")

    return render_template("home.html", name="enter valid details")


@app.route("/addvote", methods=["POST", "GET"])
def addvote():
    cand_name = request.form.get('name')
    user_details = voter.query.get(session['id'])
    user_details.status = True
    cand_details = candidate.query.get(cand_name)
    cand_details.Votes += 1
    db.session.add(cand_details)
    db.session.add(user_details)
    db.session.commit()
    session.clear()
    return jsonify({"success": True})


@ app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
