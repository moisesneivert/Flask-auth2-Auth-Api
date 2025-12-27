from flask import Flask
from app.auth.routes import auth_bp
from app.errors.handlers import register_error_handlers
from app.extensions.db import db

def create_app(testing: bool = False):
    app = Flask(__name__)
    app.config.from_object("app.core.config.Config")

    if testing:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    else:
        # default simples (você pode trocar depois por env var)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp)
    register_error_handlers(app)

    return app
