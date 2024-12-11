from . import db

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    contest_id = db.Column(db.Integer, db.ForeignKey('contests.id'))
    level = db.Column(db.String(50))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    score = db.Column(db.Numeric(5, 2))
    certificate_id = db.Column(db.Integer, db.ForeignKey('certificates.id'))
    coach_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    enrolled_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Enrollment {self.id}>'
