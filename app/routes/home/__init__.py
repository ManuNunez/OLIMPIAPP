from flask import Flask
from app.routes.home.home import home_bp
from app.routes.home.about_us import about_bp
from app.routes.home.legal import legal_bp

def init_home(app: Flask):
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(legal_bp)