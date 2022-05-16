from enum import unique
from time import timezone
from __init__ import my_database
from flask_login import UserMixin
from sqlalchemy import func
from sqlalchemy.dialects.mysql import *

class Note(my_database.Model):
    id = my_database.Column(my_database.INT, primary_key=True)
    data = my_database.Column(my_database.String(9999))
    date = my_database.Column(my_database.DateTime(timezone=True), default=func.now())
    user_id = my_database.Column(my_database.Integer, my_database.ForeignKey('user.id'))


class User(UserMixin, my_database.Model):
    id = my_database.Column(my_database.INT, primary_key=True)
    first_name = my_database.Column(my_database.VARCHAR(255))
    last_name = my_database.Column(my_database.VARCHAR(255))
    email = my_database.Column(my_database.VARCHAR(255), unique=True)
    phone = my_database.Column(my_database.VARCHAR(255), unique=True)
    password = my_database.Column(my_database.VARCHAR(255))
    notes = my_database.relationship('Note')
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}', '{self.password}')"