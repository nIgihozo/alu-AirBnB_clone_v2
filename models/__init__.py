#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    # 1. We must import the models here so SQLAlchemy "Base" sees them
    from models.state import State
    from models.city import City
    from models.user import User
    from models.place import Place
    from models.review import Review
    from models.amenity import Amenity
    # 2. NOW we can reload safely
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
