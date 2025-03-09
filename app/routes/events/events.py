from flask import Blueprint, render_template

events_bp = Blueprint('events', __name__)

@events_bp.route('/events')
def events():
    return render_template('events/events.html')