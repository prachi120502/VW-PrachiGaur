from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from models.models import User, Employee
from extensions import db

bp = Blueprint("routes", __name__)


# -----------------------
# LOGIN REQUIRED
# -----------------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return redirect(url_for("routes.login"))

        return f(*args, **kwargs)

    return wrapper


# -----------------------
# ROLE REQUIRED
# -----------------------
def role_required(*roles):
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            if session.get("role") not in roles:
                return "Unauthorized Access"

            return f(*args, **kwargs)

        return wrapper

    return decorator


# -----------------------
# LOGIN
# -----------------------
@bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username, password=password).first()

        if user:

            session["user_id"] = user.id
            session["role"] = user.role

            # Role based redirect
            if user.role == "Employee":
                return redirect(url_for("routes.employee_profile", id=user.id))
            else:
                return redirect(url_for("routes.employees"))

        return "Invalid Credentials"

    return render_template("login.html")


# -----------------------
# VIEW EMPLOYEES
# -----------------------
@bp.route("/employees")
@login_required
@role_required("Admin", "Manager")
def employees():

    if session["role"] == "Manager":

        employees = Employee.query.filter_by(
            manager_id=session["user_id"]
        ).all()

    else:

        employees = Employee.query.all()

    return render_template("employees.html", employees=employees)


# -----------------------
# VIEW EMPLOYEE PROFILE
# -----------------------
@bp.route("/employee/<int:id>")
@login_required
def employee_profile(id):

    employee = Employee.query.get_or_404(id)

    role = session["role"]
    user_id = session["user_id"]

    if role == "Employee" and user_id != id:
        return "Access Denied"

    if role == "Manager" and employee.manager_id != user_id:
        return "Access Denied"

    return render_template("employee_profile.html", employee=employee)


# -----------------------
# EDIT EMPLOYEE
# -----------------------
@bp.route("/employee/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_employee(id):

    employee = Employee.query.get_or_404(id)

    role = session["role"]
    user_id = session["user_id"]

    if role == "Employee" and user_id != id:
        return "Unauthorized"

    if role == "Manager" and employee.manager_id != user_id:
        return "Unauthorized"

    if request.method == "POST":

        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.department = request.form["department"]

        db.session.commit()

        return redirect(url_for("routes.employee_profile", id=id))

    return render_template("edit_employee.html", employee=employee)


# -----------------------
# DELETE EMPLOYEE
# -----------------------
@bp.route("/employee/<int:id>/delete")
@login_required
@role_required("Admin")
def delete_employee(id):

    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    return redirect(url_for("routes.employees"))


# -----------------------
# CREATE EMPLOYEE (ADMIN)
# -----------------------
@bp.route("/employee/create", methods=["GET", "POST"])
@login_required
@role_required("Admin")
def create_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        manager_id = request.form["manager_id"]

        emp = Employee(
            name=name,
            email=email,
            department=department,
            manager_id=manager_id
        )

        db.session.add(emp)
        db.session.commit()

        return redirect(url_for("routes.employees"))

    return render_template("create_employee.html")