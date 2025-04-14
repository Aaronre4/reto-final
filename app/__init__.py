from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_tasks.db"

    # Initialize the database
    db.init_app(app)

    # Import blueprints/routes
    from app.routes import data_routes

    # Register blueprints
    app.register_blueprint(data_routes)

    return app
