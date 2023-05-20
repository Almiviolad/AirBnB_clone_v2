#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade="all, delete, delete-orphan",
            backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter  attr to return list of cjty jnstance"""
            cities_val = models.storage.all("City").values()
            city_list = []
            for city in cities_val:
                if city.state_id == self.id:
                    city_list.append(city)
                    return city_list
