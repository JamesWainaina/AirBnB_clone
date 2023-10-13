#!/usr/bin/python3
"""this is unitest fo the Amnity class"""

import unittest
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):
    
    """the test cases for Amenity class."""
    
    def setUp(self):
        """sets up the test methods"""
        pass

    def tearDown(self):
        """it tears down the test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """It resets the filestorage data"""
        FileStorage._FileStorage_objects = {}
        if os.path.isfile(FileStorage._FileStorage_file_path):
            os.remove(FileStorage._FileStorage_file_path)

    def test_6_instantiiation(self):
        """" test instation fo Amenity class."""
        
        i = Amenity()
        self.assertEqual(str(type(i))),
        self.assertIsInstance(i, Amenity)
        self.assertTrue(issubclass(type(i),BaseModel))

    def test_attributes(self):
        """test the attributes of Amenity classe."""
        attributes = storage.attributes()["Amenity"]
        p = Amenity()
        for k , v in attributes.items():
            self.assertTrue(hasattr(p, k))
            self.assertEqual(type(getattr(p, k, None)), v)

if __name__ == "__main__":
    unittest.main()