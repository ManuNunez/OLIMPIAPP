from . import db

class School(db.Model):
    __tablename__ = 'schools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cct = db.Column(db.String(20), unique=True, nullable=False)
    longitude = db.Column(db.Numeric(9, 6))
    latitude = db.Column(db.Numeric(9, 6))

    def __repr__(self):
        return f'<School {self.name}>'
