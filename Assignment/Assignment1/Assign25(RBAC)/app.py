from flask import Flask
from config import Config
from extensions import db, migrate
from routes import bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)