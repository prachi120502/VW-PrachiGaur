from app import app
from extensions import db
from models.models import User

with app.app_context():

    admin = User(username="admin", password="123", role="Admin")

    manager = User(username="manager", password="123", role="Manager")

    employee = User(username="employee", password="123", role="Employee")

    db.session.add_all([admin, manager, employee])

    db.session.commit()

    print("Users added successfully!")