from flask import Blueprint, render_template

legal_bp = Blueprint('legal', __name__)

@legal_bp.route('/legal')
def legal():
    return render_template('home/legal.html')

