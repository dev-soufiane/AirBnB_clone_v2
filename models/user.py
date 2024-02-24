#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Class represents a user in the application."""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
