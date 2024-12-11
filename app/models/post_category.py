from . import db

class PostCategory(db.Model):
    __tablename__ = 'post_categories'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), primary_key=True)
