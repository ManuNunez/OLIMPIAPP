from flask import Flask
from app.routes.user.user import user_bp


def init_user(app: Flask):
    app.register_blueprint(user_bp)