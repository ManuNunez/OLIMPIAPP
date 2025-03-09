from flask import Flask
from .admin import admin_bp

def init_admin(app: Flask):
    app.register_blueprint(admin_bp)
