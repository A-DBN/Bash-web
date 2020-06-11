from flask import Flask, render_template, request, flash, redirect, url_for, session
import hashlib, uuid, os
from app import app
from app.controller import *

import mysql.connector as MS
connection = MS.connect(user='dantoine', password='michel',
host='127.0.0.1', buffered=True, database="epytodo")
cursor = connection.cursor()

app.secret_key = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def route_index():
    if "username" in session:
        return render_template("index.html", title="Epytodo", username="Profil")
    else:
        return render_template("index.html", title="Epytodo")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user_id = uuid.uuid4()
        username = request.form["username"]
        password = request.form["password"]
        return control_register(username, password)
    return render_template("register.html", title="Register")

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return control_login(username, password)
    else:
        if "username" in session:
            flash("Already Logged In !")
            return redirect(url_for("infos"))
        return (render_template("login.html", title="Sign in"))

@app.route('/user', methods=["GET", "POST"])
def infos():
    if request.method == "GET" and "username" in session:
        username = session["username"]
        return control_info(username)
    else:
        flash("You are not logged in !")
        return redirect(url_for("login"))

@app.route('/Team', methods=["POST", "GET"])
def team():
    return (render_template("team.html", title="Team"))

@app.route('/subject', methods=["POST", "GET"])
def subject():
    return (render_template("subject.html", title="Subject"))

@app.route('/logout')
def logout():
    flash("You have been logged out !")
    session.pop("username", None)
    return redirect(url_for("login"))
