#!/usr/bin/python3
"""This module defines the base model class."""

from datetime import datetime
import uuid
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime, Column


Base = declarative_base()

class BaseModel:
    """BaseModel class from which other classes inherit."""
    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns official string representation."""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute (updated_at.)"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object."""
        data = self.__dict__.copy()
        data["__class__"] = type(self).__name__
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()

        if '_sa_instance_state' in data.keys():
            data.pop('_sa_instance_state', None)

        return data

    def delete(self):
        """Delete the current instance from storage."""
        storage.delete(self)
