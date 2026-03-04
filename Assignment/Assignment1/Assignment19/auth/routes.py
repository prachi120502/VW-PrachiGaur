from flask import render_template, request, redirect, make_response
from . import auth_bp

# Sample users database
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "emp": {"password": "emp123", "role": "employee"},
    "hr": {"password": "hr123", "role": "hr"}
}


@auth_bp.route("/")
def login_page():
    return render_template("login.html", error="")


@auth_bp.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("role")
    remember = request.form.get("remember_me")

    # Username validation
    if username not in users:
        return render_template("login.html", error="Invalid Username")

    # Password validation
    if users[username]["password"] != password:
        return render_template("login.html", error="Incorrect Password")

    # Role validation
    if users[username]["role"] != role:
        return render_template("login.html", error="Role mismatch")

    response = make_response(redirect(f"/{role}/dashboard"))

    # Remember me checked → cookie 7 days
    if remember:
        response.set_cookie("username", username, max_age=60*60*24*7)
        response.set_cookie("user_role", role, max_age=60*60*24*7)

    # Remember me unchecked → session cookie
    else:
        response.set_cookie("username", username)
        response.set_cookie("user_role", role)

    return response


@auth_bp.route("/logout")
def logout():

    response = make_response(redirect("/"))

    response.set_cookie("username", "", expires=0)
    response.set_cookie("user_role", "", expires=0)

    return response