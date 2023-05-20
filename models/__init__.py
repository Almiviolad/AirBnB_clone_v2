#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

from os import getenv
if getenv('HBNB_TYPE_STORAGE') == "db":
=======
import os


type_storage = os.getenv('HBNB_TYPE_STORAGE')


if type_storage == "db":
    from models.engine.db_storage import DBStorage
>>>>>>> 82da1cde10326cbee2cfe65b71bd18eed974df2b
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
