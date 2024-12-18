from flask import Flask
from app.routes.utils.schools import school_bp

def init_utils(app: Flask):
    app.register_blueprint(school_bp)
