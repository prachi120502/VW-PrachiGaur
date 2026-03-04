from flask import Flask
from auth.routes import auth_bp
from admin.routes import admin_bp
from employee.routes import employee_bp
from hr.routes import hr_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(hr_bp)

if __name__ == "__main__":
    app.run(debug=True)