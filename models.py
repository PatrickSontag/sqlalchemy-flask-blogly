"""Models for Blogly."""

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
        return f"<User id={self.id}, first name={self.first_name}, last name={self.last_name}, image={self.image_url}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    last_name = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    image_url = db.Column(db.String(),
                    nullable=True,
                    unique=False,
                    default="/user_profile_pics/default_user_profile.jpg")

    