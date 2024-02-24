#!/usr/bin/python3
"""This module defines the State class."""

from os import getenv
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """Class represents a state in the application."""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
