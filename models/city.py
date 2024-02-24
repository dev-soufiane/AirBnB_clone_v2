#!/usr/bin/python3
"""This module defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that represents a city for the application."""
    state_id = ""
    name = ""
