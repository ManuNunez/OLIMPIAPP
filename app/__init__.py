from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import get_config
from app.routes import init_app

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    

  
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    

    init_app(app)


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('development/under_development.html'), 404
    
    return app
