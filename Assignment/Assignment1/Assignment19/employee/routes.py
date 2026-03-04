from flask import request, redirect, render_template
from . import employee_bp


@employee_bp.route("/dashboard")
def dashboard():

    role = request.cookies.get("user_role")
    username = request.cookies.get("username")

    if not role or role != "employee":
        return redirect("/")

    return render_template("employee_dashboard.html", username=username)