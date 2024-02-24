#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class represents a user in the application."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
