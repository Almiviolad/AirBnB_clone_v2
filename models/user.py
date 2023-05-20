#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """user class model"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade='all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan', backref="user")
