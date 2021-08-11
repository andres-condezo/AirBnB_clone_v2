#!/usr/bin/ỳthon3
"""test for the console"""

import unittest

from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):

    def test_prompt(self):
        """ Test for the name in the prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)
