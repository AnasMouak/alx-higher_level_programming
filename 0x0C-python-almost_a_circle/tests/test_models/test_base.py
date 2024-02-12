#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseID(unittest.TestCase):
    """
    Test case class to validate the ID generation of Base class.
    """
    def test_id0(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id(self):
        b1 = Base()
        b2 = Base(4)
        self.assertEqual(b1.id, b2.id - 3)
    
    def test_id1(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1) 

    def test_id2(self):
        self.assertEqual(Base(5).id, 5)

    def test_float_id(self):
        self.assertEqual(Base(5.5).id, 5.5)
    
    def test_str_id(self):
        self.assertEqual(Base("anas").id, "anas")

    def test_bool_id(self):
        self.assertEqual(Base(True).id, True)

    def test_list_id(self):
        self.assertEqual(Base([5, 4, 2]).id, [5, 4, 2])

    def test_tuple_id(self):
        self.assertEqual(Base((5.5, 4, 3)).id, (5.5, 4, 3))

    def test_set_id(self):
        self.assertEqual(Base({5.5, 6, 7}).id, {5.5, 6, 7})

    def test_dict_id(self):
        self.assertEqual(Base({"a": 5.5, "b": 6}).id, {"a": 5.5, "b": 6})

    def test_error_id(self):
        with self.assertRaises(TypeError):
            Base(5, 4)

class TestBase_tojsonString(unittest.TestCase):
    """
    Test case class to validate the to_json_string method of Base class.
    """
    def test_rectangle_tojsonStr(self):
        r = Rectangle(10, 7, 2, 8, 1)
        correct = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string([r.to_dictionary()]), correct)
    
    def test_rectangle_tojsonStr2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        list_dict = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 106)

    def test_square_tojsonStr(self):
        s = Square(10, 1, 2, 1)
        correct = '[{"id": 1, "size": 10, "x": 1, "y": 2}]'
        self.assertEqual(Base.to_json_string([s.to_dictionary()]), correct)

    def test_square_tojsonStr2(self):
        s1 = Square(10, 1, 2, 1)
        s2 = Square(10, 1, 2, 1)
        list_dict = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 78)
    
    def test_tojsonStrNone(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_tojsonStrempty(self):
        self.assertEqual(Base.to_json_string([]), "[]")
    
    def test_error_json(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()
    
    def test_error_json2(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 5)

class TestBase_Savetofile(unittest.TestCase):
    """
    Test case class to validate the save_to_file method of Base class.
    """
    def test_jsonStrFile_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(content, correct)
    
    def test_jsonStrFile_Rectangle1(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Base.save_to_file([r1])
        with open("Base.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(content, correct)
    
    def test_jsonStrFile_Rectangle2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertTrue(len(content) == 106)

    def test_jsonStrFile_Rectangle3(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(10, 7, 2, 8, 2)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 2, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(content, correct)

    def test_jsonStrFile_Square(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file([s1])
        with open("Square.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 1, "size": 10, "x": 2, "y": 2}]'
        self.assertEqual(content, correct)
    
    def test_jsonStrFile_Square1(self):
        s1 = Square(10, 2, 2, 1)
        Base.save_to_file([s1])
        with open("Base.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 1, "size": 10, "x": 2, "y": 2}]'
        self.assertEqual(content, correct)
    
    def test_jsonStrFile_Square2(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(10, 7, 2, 1)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertTrue(len(content) == 78)
    
    def test_jsonStrFile_Square3(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file([s1])
        s2 = Square(10, 2, 2, 2)
        Square.save_to_file([s2])
        with open("Square.json", "r", encoding="utf-8") as f:
            content = f.read()
        correct = '[{"id": 2, "size": 10, "x": 2, "y": 2}]'
        self.assertEqual(content, correct)

    def test_jsonStrFile_RectangleNone(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_jsonStrFile_SquareNone(self):
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "[]")
    
    def test_error_savetofile(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
    
    def test_error_savetofile2(self):
        r = Rectangle(10, 7, 2, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([r], 5)
    
    def test_error_savetofile3(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()
    
class TestBase_fromjsonString(unittest.TestCase):
    """
    Test case class to validate the from_json_string method of Base class.
    """
    def test_rectangle_fromjsonStr(self):
        input = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        json_input = Rectangle.to_json_string(input)
        output = Rectangle.from_json_string(json_input)
        self.assertEqual(input, output)
    
    def test_rectangle_fromjsonStr2(self):
        input = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 5, "height": 7, "x": 2, "y": 1},
        ]
        json_input = Rectangle.to_json_string(input)
        output = Rectangle.from_json_string(json_input)
        self.assertEqual(input, output)

    def test_square_fromjsonStr(self):
        input = [{"id": 1, "size": 7, "x": 2, "y": 2}]
        json_input = Square.to_json_string(input)
        output = Square.from_json_string(json_input)
        self.assertEqual(input, output)

    def test_square_fromjsonStr2(self):
        input = [
            {"id": 1, "size": 7, "x": 2, "y": 2},
            {"id": 2, "size": 5, "x": 2, "y": 1},
        ]
        json_input = Square.to_json_string(input)
        output = Square.from_json_string(json_input)
        self.assertEqual(input, output)
    
    def test_fromjsonStrNone(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_fromjsonStrempty(self):
        self.assertEqual(Base.from_json_string("[]"), [])
    
    def test_error_json(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()
    
    def test_error_json2(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 5)
    
class TestBase_create(unittest.TestCase):
    """
    Test case class to validate the creation of objects
    using the create class method.
    """
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/2 - 3/5")
    
    def test_create_rectangle1(self):
        r1 = Rectangle(3, 5, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
    
    def test_create_rectangle2(self):
        r1 = Rectangle(3, 5, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        r1 = Square(3, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Square] (1) 1/2 - 3")
    
    def test_create_square1(self):
        r1 = Square(3, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
    
    def test_create_square2(self):
        r1 = Square(3, 1, 2, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

class TestBase_Loadfromfile(unittest.TestCase):
    """
    Test case class to validate loading objects from JSON files
    for Rectangle and Square classes.
    """
    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
    
    def test_jsonStrFile_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), output[0].__str__())
    
    
    def test_jsonStrFile_Rectangle1(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), output[1].__str__())
    
    def test_jsonStrFile_RectangleType(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_jsonStrFile_Square(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file([s1])
        output = Square.load_from_file()        
        self.assertEqual(s1.__str__(), output[0].__str__())
    
    def test_jsonStrFile_Square1(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(10, 7, 2, 1)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()        
        self.assertEqual(s1.__str__(), output[1].__str__())
    
    def test_jsonStrFile_SquareType(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(10, 7, 2, 1)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()        
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_jsonStrFile_RectangleNone(self):
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_jsonStrFile_SquareNone(self):
        output = Square.load_from_file()
        self.assertEqual([], output)
    
    def test_error_loadfromfile(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], 5)
    
class TestBase_Savetofile_csv(unittest.TestCase):
    """
    Test case class to validate saving objects to CSV files
    for Rectangle and Square classes.
    """
    def test_csvStrFile_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "1,10,7,2,8\n"
        self.assertEqual(content, correct)
    
    def test_csvStrFile_Rectangle1(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(5, 2, 2, 1, 2)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "1,10,7,2,8\n2,5,2,2,1\n"
        self.assertEqual(content, correct)

    def test_csvStrFile_Rectangle2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        r2 = Rectangle(10, 7, 2, 8, 2)
        Rectangle.save_to_file_csv([r2])
        with open("Rectangle.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "2,10,7,2,8\n"
        self.assertEqual(content, correct)

    def test_csvStrFile_Square(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file_csv([s1])
        with open("Square.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "1,10,2,2\n"
        self.assertEqual(content, correct)
    
    def test_csvStrFile_Square1(self):
        s1 = Square(10, 2, 2, 1)
        Base.save_to_file_csv([s1])
        with open("Base.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "1,10,2,2\n"
        self.assertEqual(content, correct)
    
    def test_csvStrFile_Square2(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(5, 2, 2, 2)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "1,10,7,2\n2,5,2,2\n"
        self.assertEqual(content, correct)
    
    def test_csvStrFile_Square3(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file_csv([s1])
        s2 = Square(10, 2, 2, 2)
        Square.save_to_file_csv([s2])
        with open("Square.csv", "r", encoding="utf-8") as f:
            content = f.read()
        correct = "2,10,2,2\n"
        self.assertEqual(content, correct)

    def test_csvStrFile_RectangleNone(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "[]")

    def test_csvStrFile_SquareNone(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertEqual(content, "[]")
    
    def test_error_savetofile_csv(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
    
    def test_error_savetofile_csv2(self):
        r = Rectangle(10, 7, 2, 8, 1)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([r], 5)
    
    def test_error_savetofile_csv3(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()

class TestBase_Loadfromfile_csv(unittest.TestCase):
    """
    Test case class to validate loading objects from CSV files
    for Rectangle and Square classes.
    """
    @classmethod
    def tearDown(self):
        """
        Clean up any created files after each test method.
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
    
    def test_csvStrFile_Rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(r1.__str__(), output[0].__str__())
    
    
    def test_csvStrFile_Rectangle1(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(r1.__str__(), output[1].__str__())
    
    def test_csvStrFile_RectangleType(self):

        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_csvStrFile_Square(self):
        s1 = Square(10, 2, 2, 1)
        Square.save_to_file_csv([s1])
        output = Square.load_from_file_csv()        
        self.assertEqual(s1.__str__(), output[0].__str__())
    
    def test_csvStrFile_Square1(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(10, 7, 2, 1)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()        
        self.assertEqual(s1.__str__(), output[1].__str__())
    
    def test_csvStrFile_SquareType(self):
        s1 = Square(10, 7, 2, 1)
        s2 = Square(10, 7, 2, 1)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()        
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_csvStrFile_RectangleNone(self):
        output = Rectangle.load_from_file_csv()
        self.assertEqual(output, [])

    def test_csvStrFile_SquareNone(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)
    
    def test_error_loadfromfile(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv([], 5)

