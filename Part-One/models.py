"""SQLAlchemy Models for Blogly"""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.Text, nullable = False)
    last_name = db.Column(db.Text, nullable = False)
    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Returns the User's Full Name"""
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connects the Database to the Provided Flask App"""
    db.app = app
    db.init_app(app)