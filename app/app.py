from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import get_user_by_username, create_user, save_prediction
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "fraudshield-secret-key"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if get_user_by_username(username):
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        hashed = generate_password_hash(password)
        create_user(username, hashed)
        flash("Account created. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user_by_username(username)

        if not user or not check_password_hash(user["password"], password):
            flash("Invalid username or password.", "error")
            return redirect(url_for("login"))

        session["user_id"] = user["id"]
        session["username"] = user["username"]
        return redirect(url_for("dashboard"))

    return render_template("login.html")
