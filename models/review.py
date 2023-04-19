#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    place_id = Column(String(60), nullable=False, foreign_key(place.id))
    user_id =Column(String(60), nullable=False, foreign_key(users.id))
    text = Column(String(1024), nullable=False)
