from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory employee data
employees = [
    {"name": "Priya", "dept": "HR", "salary": 80000},
    {"name": "Rohan", "dept": "SAP", "salary": 70000},
    {"name": "Zalak", "dept": "AI", "salary": 75000}
]

@app.route("/")
def home():
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    global employees

    role = request.args.get("role", "employee").lower()
    delete_name = request.args.get("delete")

    # Admin delete logic
    if role == "admin" and delete_name:
        employees = [
            emp for emp in employees
            if emp["name"] != delete_name
        ]
        return redirect(url_for("dashboard", role="admin"))

    return render_template("dashboard.html", role=role, employees=employees)

if __name__ == "__main__":
    app.run(debug=True)