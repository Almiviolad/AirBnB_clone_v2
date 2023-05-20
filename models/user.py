#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """user class model"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, pwd):
        """hashing password values"""
        self._password = pwd
