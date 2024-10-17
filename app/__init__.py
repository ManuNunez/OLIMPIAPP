from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

  
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    

    # Registro de Blueprints

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('under_development.html'), 404
    
    return app
