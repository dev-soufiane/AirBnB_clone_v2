#!/usr/bin/python3
"""
This module initializes the package and sets up the storage.
"""

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
