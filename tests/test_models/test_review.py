#!/usr/bin/python3
"""Defines the unittest module for the review class"""

import unittest
import os
import json
from models.review import Review
import re
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import time
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Class test for review class."""

    def setUp(self):
        """Method to set up test."""
        pass

    def tearDown(self):
        """Method to tear down."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Methods to reset the filestorage."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Method to check instances of review class."""
        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Method to check attributes of review class."""
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
