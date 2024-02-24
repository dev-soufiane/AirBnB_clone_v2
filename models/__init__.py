#!/usr/bin/python3
"""
This module initializes the package and sets up the storage.
"""

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload the storage
storage.reload()
