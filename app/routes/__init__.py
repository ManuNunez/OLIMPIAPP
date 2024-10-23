from flask import Flask
from app.routes.home import init_home
# from app.routes.admin import init_admin
# from app.routes.auth import init_auth
# from app.routes.public import init_public
# from app.routes.user import init_user

def init_app(app: Flask):
    init_home(app)
    # init_admin(app)
    # init_auth(app)
    # init_public(app)
    # init_user(app)
