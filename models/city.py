#!/usr/bin/python3
"""This module defines the City class."""

from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class that represents a city for the application."""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref='cities',
                          cascade='all, delete-orphan')
