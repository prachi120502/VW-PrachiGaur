from flask import request, redirect, render_template
from . import admin_bp


@admin_bp.route("/dashboard")
def dashboard():

    role = request.cookies.get("user_role")
    username = request.cookies.get("username")

    if not role or role != "admin":
        return redirect("/")

    return render_template("admin_dashboard.html", username=username)