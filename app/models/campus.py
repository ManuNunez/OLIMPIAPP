from . import db

class Campus(db.Model):
    __tablename__ = 'campus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Campus {self.name}>'
