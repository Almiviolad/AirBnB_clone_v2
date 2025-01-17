#!/usr/bin/python3
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Representation of Amenity """
#    if getenv('HBNB_TYPE_STORAGE') == 'db':
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
#    def __init__(self, *args, **kwargs):
#        """initializes Amenity"""
#        super().__init__(*args, **kwargs)
