from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .role import Role
from .school import School
from .campus import Campus
from .contest import Contest
from .user import User
from .certificate import Certificate
from .enrollment import Enrollment
from .post import Post
from .category import Category
from .comment import Comment
from .post_category import PostCategory
