#!/usr/bin/python3
"""Unittests for the Base Class"""

import os
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Cases for Instantation of the base class"""

    def test_unique_id(self):
        # Ensure each instance of Base has a unique id
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b2.id, b3.id)

    def test_provided_id(self):
        # Ensure provided id is assigned correctly
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_increment_id(self):
        # Ensure id is incremented for each new instance without provided id
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)


if __name__ == '__main__':
    unittest.main()
