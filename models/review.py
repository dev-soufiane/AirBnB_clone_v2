#!/usr/bin/python3
"""This module defines the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that represents a review for a place in the application."""
    place_id = ""
    user_id = ""
    text = ""
