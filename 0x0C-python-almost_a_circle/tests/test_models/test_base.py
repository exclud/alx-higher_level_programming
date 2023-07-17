#!/usr/bin/python3
"""Unittests for the Base Class"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    def test_initialization_with_id(self):
        base = Base(10)
        self.assertEqual(base.id, 10)


    def test_to_json_string_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        json_string = Base.to_json_string([rectangle.to_dictionary()])
        expected_json = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(json_string, expected_json)

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_to_file(self):
        rectangle = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_json = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
            self.assertEqual(content, expected_json)

    def test_from_json_string_empty_string(self):
        json_list = Base.from_json_string("")
        self.assertEqual(json_list, [])

    def test_from_json_string_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_string(self):
        json_string = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        json_list = Base.from_json_string(json_string)
        expected_list = [{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]
        self.assertEqual(json_list, expected_list)

    def test_create_rectangle(self):
        rectangle_dict = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_create_square(self):
        square_dict = {"id": 5, "size": 3, "x": 1, "y": 2}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_load_from_file_rectangle_exists(self):
        rectangle1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle1])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 1)
        rectangle2 = rectangles[0]
        self.assertIsInstance(rectangle2, Rectangle)
        self.assertEqual(rectangle2.id, 5)
        self.assertEqual(rectangle2.width, 1)
        self.assertEqual(rectangle2.height, 2)
        self.assertEqual(rectangle2.x, 3)
        self.assertEqual(rectangle2.y, 4)


    def test_load_from_file_square_exists(self):
        square1 = Square(3, 1, 2, 5)
        Square.save_to_file([square1])
        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 1)
        square2 = squares[0]
        self.assertIsInstance(square2, Square)
        self.assertEqual(square2.id, 5)
        self.assertEqual(square2.size, 3)
        self.assertEqual(square2.x, 1)
        self.assertEqual(square2.y, 2)

    

if __name__ == "__main__":
    unittest.main()
