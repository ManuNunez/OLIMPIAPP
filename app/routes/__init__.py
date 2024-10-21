from flask import Flask
from app.routes.home import home_bp
# from app.routes.admin import admin_bp
# from app.routes.auth import auth_bp
# from app.routes.public import public_bp
# from app.routes.user import user_bp

def init_app(app: Flask):
    app.register_blueprint(home_bp)
    # app.register_blueprint(admin_bp)
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(public_bp)
    # app.register_blueprint(user_bp)
