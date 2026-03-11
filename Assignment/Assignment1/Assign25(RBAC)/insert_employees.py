from app import app
from extensions import db
from models.models import Employee

with app.app_context():

    emp1 = Employee(
        name="Rahul",
        email="rahul@company.com",
        department="IT",
        manager_id=2
    )

    emp2 = Employee(
        name="Priya",
        email="priya@company.com",
        department="Sales",
        manager_id=2
    )

    db.session.add_all([emp1, emp2])
    db.session.commit()

    print("Employees inserted successfully")