from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# model for storing users objects in the database
class User(db.Model, UserMixin):
    # primary key for each object created
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    # define a relationship to connect user with Note
    notes = db.relationship('Note')


# model for storing note objects in database
class Note(db.Model):
    # primary key for each object created
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # automatically add the date using func.now() function
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # for each not store the id of the user who created it using a foreign key relation
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
