from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User, School  
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        curp = request.form.get('curp')
        username = request.form.get('username')
        email = request.form.get('email')
        confirm_email = request.form.get('confirm_email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        school_cct = request.form.get('school_cct')
        role = request.form.get('role')

        if not name or not curp or not username or not email or not password or not school_cct:
            flash('All fields are required!', 'error')
            return redirect(url_for('auth.sign_up'))

        if email != confirm_email:
            flash('Emails do not match!', 'error')
            return redirect(url_for('auth.sign_up'))

        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('auth.sign_up'))

        school = School.query.filter_by(cct=school_cct).first()
        if not school:
            flash('Invalid school CCT!', 'error')
            return redirect(url_for('auth.sign_up'))

        
        existing_user = User.query.filter((User.username == username)).first()
        if existing_user:
            flash('Username already exists!', 'error')
            return redirect(url_for('auth.sign_up'))

        new_user = User(
            name=name,
            curp=curp,
            username=username,
            email=email,
            password_hash=password, 
            school_id=school.id  
        )
 
        db.session.add(new_user)
        db.session.commit()

        

        flash('Account created successfully!', 'success')
        return redirect(url_for('home.index'))

    return render_template('auth/sign_up.html')


