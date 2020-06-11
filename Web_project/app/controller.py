from flask import render_template, request, flash, redirect, url_for, session
from app.models import *

def control_login(username, password):
    res = bdd_login(username, password)
    if len(res) == 0:
        session['username'] = None
        error = "Ce username ou ce mot de passe ne sont pas valides, veuillez reessayer"
        return render_template("login.html", error=error)
    else:
        session["username"] = request.form["username"]
        return redirect(url_for("infos"))

def control_info(username):
    res = bdd_info(username)
    return render_template("infos.html",
                           resultat_requete_information_client=res)

def control_register(username, password):
    bdd_register(username, password)
    return redirect(url_for("login"))
