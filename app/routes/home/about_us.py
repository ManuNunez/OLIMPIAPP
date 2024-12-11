from flask import Blueprint, render_template

about_bp = Blueprint('about-us', __name__)


@about_bp.route('/about-us')
def about():
    return render_template('home/about.html')
