#!/usr/bin/python3
"""FileStorage utility class."""

import os
import datetime
import json


class FileStorage:
    """Manages object storage and retrieval."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the entire object dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes and writes stored objects to a JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            s_data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(s_data, file)

    def classes(self):
        """Returns a mapping of class names to their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_references = {"BaseModel": BaseModel,
                            "User": User,
                            "State": State,
                            "City": City,
                            "Amenity": Amenity,
                            "Place": Place,
                            "Review": Review}
        return class_references

    def reload(self):
        """Reloads stored objects from the JSON file."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            stored_data = json.load(file)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in stored_data.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns attributes and types for each class."""
        attributes = {
            "BaseModel": {"id": str,
                          "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
            "User": {"email": str,
                     "password": str,
                     "first_name": str,
                     "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str,
                     "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review": {"place_id": str,
                       "user_id": str,
                       "text": str}
        }
        return attributes
