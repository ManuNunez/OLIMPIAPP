from flask import Flask
from app.routes.events.events import events_bp


def init_events(app: Flask):
    app.register_blueprint(events_bp)