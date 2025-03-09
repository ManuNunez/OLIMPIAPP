from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
def profile():
    return render_template('user/profile.html')

@user_bp.route('/professors')
def professors():
    return render_template('user/professors.html')

@user_bp.route('/students')
def students():
    return render_template('user/students.html')