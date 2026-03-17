from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User
from extensions import db

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET","POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(name=name,email=email,password=password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.login"))

    return render_template("signup.html")


@auth.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email,password=password).first()

        if user:
            return redirect("/dashboard")

    return render_template("login.html")