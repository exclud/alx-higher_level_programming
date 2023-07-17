#!/usr/bin/python3
"""Test Cases for the rectangle"""
import os
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_initialization(self):
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_width_property(self):
        r = Rectangle(5, 10)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("5", 10)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 10)

    def test_height_property(self):
        r = Rectangle(5, 10)
        r.height = 12
        self.assertEqual(r.height, 12)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, "10")
        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10)

    def test_x_property(self):
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10)
            r.x = "3"
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10)
            r.x = -3

    def test_y_property(self):
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10)
            r.y = "4"
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10)
            r.y = -4

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        r = Rectangle(5, 10, 1, 2, 3)
        expected_str = "[Rectangle] (3) 1/2 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_update_no_keyword_args(self):
        r = Rectangle(5, 10)
        r.update(2, 7, 8, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_keyword_args(self):
        r = Rectangle(5, 10)
        r.update(id=2, width=7, height=8, x=3, y=4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_mixed_args(self):
        r = Rectangle(5, 10)
        r.update(2, 7, y=4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 4)


if __name__ == '__main__':
    unittest.main()