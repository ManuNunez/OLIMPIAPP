from . import db
from .user_role import UserRole

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120))
    curp = db.Column(db.String(18), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __init__(self, name, curp, username, email, password_hash, school_id):
        self.name = name
        self.curp = curp
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.school_id = school_id

    def add_default_role(self):
        default_roles = [10, 11]
        for role_id in default_roles:
            user_role = UserRole(user_id=self.id, role_id=role_id)
            db.session.add(user_role)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.name}>'
    

