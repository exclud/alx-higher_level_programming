#!/usr/bin/python3
"""Test Cases for the rectangle"""
import os
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_attributes(self):
        r = Rectangle(4, 6, 2, 2, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 1)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 6, 2, 2, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 6, 2, 2, 1)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -6, 2, 2, 1)
        with self.assertRaises(ValueError):
            Rectangle(4, 0, 2, 2, 1)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, -2, 2, 1)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, 2, -2, 1)

    def test_area(self):
        r = Rectangle(4, 6, 2, 2, 1)
        self.assertEqual(r.area(), 24)

    def test_display(self):
        r = Rectangle(4, 6, 2, 2, 1)
        expected_output = "  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        with self.assertLogs() as logs:
            r.display()
            self.assertEqual(logs.output[0], expected_output)

    def test_string_representation(self):
        r = Rectangle(4, 6, 2, 2, 1)
        expected_output = "[Rectangle] (1) 2/2 - 4/6"
        self.assertEqual(str(r), expected_output)


if __name__ == '__main__':
    unittest.main()
