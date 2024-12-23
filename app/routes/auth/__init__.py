from flask import Flask
from app.routes.auth.auth import auth_bp

def init_auth(app: Flask):
    app.register_blueprint(auth_bp)