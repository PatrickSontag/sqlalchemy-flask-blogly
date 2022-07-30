"""Models for Blogly."""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_USER_IMAGE = "default_user_profile.jpg"

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User"""
    __tablename__ = "users"

    def __repr__(self):
        return f"<User id={self.id}, first name={self.first_name}, last name={self.last_name}, image={self.image}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    image = db.Column(db.String(),
                    nullable=False,
                    unique=False)

    posts = db.relationship('Post')

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    # def __repr__(self):
        # return f<

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    title = db.Column(db.String(50),
                nullable=False,
                unique=False)
    content = db.Column(db.String(500),
                nullable=False,
                unique=False)
    created_at = db.Column(db.DateTime,
                nullable=False,
                default=datetime.datetime.now)
    user_id = db.Column(db.Integer, 
                db.ForeignKey('users.id'),
                nullable=False)

    user = db.relationship('User')
    # could also use "backref" to create two-way connection between Models

class Tag(db.Model):
    """Tag in a post"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

class PostTag(db.Model):
    """Post and Tag jointable"""

    __tablename__ = "post_tag"

    posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)


#   ---------FUNCTIONS----------------  

def user_posts_join_class():
    """Show employees with a join.
    """

    posts = (db.session.query(Post, User)
            .join(User).all())

    for post, user in posts:  # [(<P>, <U>), (<P>, <U>)]
        print(user.first_name, user.last_name, ":", post.title, "-", post.content)
