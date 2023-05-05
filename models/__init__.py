#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
=======
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
>>>>>>> 47b17018372f604fe72ac18c9cc99c1c84c0dd94
from os import getenv
if getenv('HBNB_TYPE_STORAGE') == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
