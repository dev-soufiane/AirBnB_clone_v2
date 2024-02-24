#!/usr/bin/python3
"""Defines the unittest module for the city class"""

import unittest
import os
import json
from models.city import City
import re
from models import storage
from models.base_model import BaseModel
from datetime import datetime
import time
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Class test for city class."""

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
        """Method to check instances of city class."""
        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Method to check attributes of city class."""
        attributes = storage.attributes()["City"]
        o = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()
