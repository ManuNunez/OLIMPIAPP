from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import db, User, School, UserRole, Role

from app.decorators.redirect_authenticated import redirect_authenticated

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/sign-up', methods=['POST', 'GET'])
@redirect_authenticated
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

        
        new_user = User(name, curp, username, email, password, school.id)
 
        db.session.add(new_user)
        db.session.commit()
        new_user.add_default_role()
        
        #Se obtienen los roles del usuario y se le asignan a la sesion asi como el user_id
        user_roles = db.session.query(Role.name).join(UserRole).join(User).filter(User.id == new_user.id).all()
        roles_list = [role[0] for role in user_roles]

        session['user_id'] = new_user.id
        session['role'] = roles_list

        session.permanent = True

        flash('Account created successfully!', 'success')
        return redirect(url_for('home.index'))

    return render_template('auth/sign_up.html')



@auth_bp.route('/login', methods=['GET', 'POST'])
@redirect_authenticated
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        #Si las credenciales son correctas, se obtiene los roles del usuario y se le asigna a la sesion asi como el user_id
        if user and user.check_password(password):
            roles = db.session.query(Role.name)\
                .join(UserRole, Role.id == UserRole.role_id)\
                .filter(UserRole.user_id == user.id).all()
            
            roles_list = [role[0] for role in roles]  

            session['user_id'] = user.id
            session['role'] = roles_list
            
            session.permanent = True
        elif not user or not user.check_password(password):
            flash('Invalid credentials', 'error')
            return redirect(url_for('auth.login'))
        return redirect(url_for('home.index'))

    return render_template('auth/login.html')

#Se limpia la cookie al salir de la sesion
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()

    flash('You have been logged out successfully!', 'success')
    return redirect(url_for('home.index'))
