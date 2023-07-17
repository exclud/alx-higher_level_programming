#!/usr/bin/python3
"""Test Cases for the Square"""

import os
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_square_str(self):
        square = Square(5, 2, 3, 10)
        expected_output = "[Square] (10) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_square_update_no_args(self):
        square = Square(5, 2, 3, 10)
        square.update()
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_square_update_args(self):
        square = Square(5, 2, 3, 10)
        square.update(20, 10, 5, 6)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 6)

    def test_square_update_kwargs(self):
        square = Square(5, 2, 3, 10)
        square.update(id=30, size=8, x=4, y=2)
        self.assertEqual(square.id, 30)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 2)

    def test_square_to_dictionary(self):
        square = Square(5, 2, 3, 10)
        expected_dict = {
            "id": 10,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(square.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
