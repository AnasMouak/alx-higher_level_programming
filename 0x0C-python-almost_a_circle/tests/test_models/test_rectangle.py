#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle

class TestRectangleID_Attr(unittest.TestCase):
    """
    Test cases for the Rectangle class attributes and ID assignment.
    """
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(1, 2, 3), Base)

    def test_id0(self):
        r1 = Rectangle(3, 4)
        r2 = Rectangle(2, 1)
        r3 = Rectangle(5, 5, 7, 6)
        self.assertEqual(r1.id, r3.id - 2)

    def test_id1(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_id2(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_error_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_error_arg2(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_error_arg3(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 13)
    
    def test_Getwidth(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).width, 10)

    def test_Getheight(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).height, 2)

    def test_Getx(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).x, 0)
    
    def test_Gety(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).y, 0)

    def test_Setwidth(self):
        r = Rectangle(10, 2, 0, 0, 12)
        r.width = 4
        self.assertEqual(r.width, 4)

    def test_Setheight(self):
        r = Rectangle(10, 2, 0, 0, 12)
        r.height = 3
        self.assertEqual(r.height, 3)

    def test_Setx(self):
        r = Rectangle(10, 2, 0, 0, 12)
        r.x = 3
        self.assertEqual(r.x, 3)
    
    def test_Sety(self):
        r = Rectangle(10, 2, 0, 0, 12)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_prvAttr_width(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 0, 0, 12).__width

    def test_prvAttr_height(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 0, 0, 12).__height

    def test_prvAttr_x(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 0, 0, 12).__x
    
    def test_prvAttr_y(self):
        with self.assertRaises(AttributeError):
            Rectangle(10, 2, 0, 0, 12).__y
    
class TestRectangleType_ValueError(unittest.TestCase):
    """
    Test cases for verifying error handling in the Rectangle class constructor.
    """
    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
    
    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.1, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
    
    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"10": 1, "11": 2}, 2)
    
    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
    
    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.1)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (1, 2, 3))
    
    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"10": 1, "11": 2})
    
    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {1, 2, 3})
    
    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 1, "2")
    
    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, -1.1)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, (1, 2, 3))
    
    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 11, {"10": 1, "11": 2})
    
    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, {1, 2, 3})
    
    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 2, None)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -2)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 1, 1, "2")
    
    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 2, -1.1)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 3, (1, 2, 3))
    
    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 11, 2, {"10": 1, "11": 2})
    
    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 3, {1, 2, 3})
    
    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 2, 4, None)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 2, -2)


    def test_heightErr(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "-1", "2")
    
    def test_widthErr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2, -1.1)

    def test_xErr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, "-3", [1, 2, 3])

    def test_widthErr2(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 2, (1, 2, 3), "anas")
    
    def test_heightErr2(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -11, {"10": 1, "11": 2})
    
    def test_xErr2(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -2, -1)

class TestRectangle_Area(unittest.TestCase):
    """
    Test case class to validate the area method of Rectangle class.
    """
    def test_area(self):
        self.assertEqual(Rectangle(1, 2).area(), 2)

    def test_area1(self):
        self.assertEqual(Rectangle(3, 2, 3, 4).area(), 6)

    def test_area2(self):
        r = Rectangle(3, 2, 3, 4)
        r.width = 6
        r.height = 5
        self.assertEqual(r.area(), 30)
    
    def test_areaErr(self):
        r = Rectangle(1, 2, 2, 1)
        with self.assertRaises(TypeError):
            r.area(4)

class TestRectangle_Display(unittest.TestCase):
    """
    Test case class to validate the display method of Rectangle class.
    """
    def test_display1(self):
        r = Rectangle(2, 2) 
        self.assertEqual(r.display(), "##\n##\n")
    
    def test_display2(self):
        r = Rectangle(4, 2) 
        self.assertEqual(r.display(), "####\n####\n")

    def test_displayErr(self):
        r = Rectangle(1, 2, 2, 1)
        with self.assertRaises(TypeError):
            r.display(4)
    
    def test_display_with_position1(self):
        r = Rectangle(2, 2, 1, 1) 
        self.assertEqual(r.display(), "\n ##\n ##\n")
    
    def test_display_with_position2(self):
        r = Rectangle(2, 2, 2, 0) 
        self.assertEqual(r.display(), "  ##\n  ##\n")
    
    def test_display_with_position3(self):
        r = Rectangle(4, 2, 0, 2) 
        self.assertEqual(r.display(), "\n\n####\n####\n")

class TestRectangle_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Rectangle class.
    """
    def test_str1(self):
        r = Rectangle(2, 2, 2, 0) 
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 2/0 - 2/2")
    
    def test_str11(self):
        r = Rectangle(2, 2, 2) 
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 2/0 - 2/2")

    def test_str2(self):
        r = Rectangle(2, 2) 
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 0/0 - 2/2")
    
    def test_str3(self):
        r = Rectangle(2, 2, 2, 0, 4) 
        self.assertEqual(r.__str__(), f"[Rectangle] (4) 2/0 - 2/2")
    
    def test_str4(self):
        r = Rectangle(2, 2, 2, 0, (1, 4))
        r.width = 4
        r.height = 4
        r.x = 1
        r.y = 1
        self.assertEqual(r.__str__(), f"[Rectangle] ((1, 4)) 1/1 - 4/4")
    
    def test_strErr(self):
        r = Rectangle(1, 2, 2, 1, 2)
        with self.assertRaises(TypeError):
            r.__str__(4)
    
class TestRectangle_Update(unittest.TestCase):
    """
    Test case class to validate the update method of Rectangle class.
    """
    def test_update1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 2/0 - 2/2")
    
    def test_update2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 2/0 - 6/2")

    def test_update3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6, 9)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 2/0 - 6/9")
    
    def test_update4(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6, 9, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 1/0 - 6/9")
    
    def test_update5(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6, 9, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 1/1 - 6/9")
    
    def test_update6(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6, 9, 1, 1)
        r.update(3, 5, 3, 1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 1/1 - 5/3")
    
    def test_update7(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(2, 6, 9, 1, 1)
        r.update(None, 5, 3, 1, 1)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 1/1 - 5/3")
    
    def test_updateErrWidth1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(4, "1")
        
    def test_updateErrWidth2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(4, 0)
    
    def test_updateErrWidth3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(4, -1)
    
    def test_updateErrheight1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(4, 2, "1")
        
    def test_updateErrheight2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(4, 2, 0)
    
    def test_updateErrheight3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(4, 2, -1)
    
    def test_updateErrX1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(4, 2, 2, "1")
        
    def test_updateErrX2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(4, 2, 2, -1)

    def test_updateErrY1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(4, 2, 2, 1, "1")
        
    def test_updateErrY2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(4, 2, 2, 1, -1)

    def test_update_kwargs1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (7) 2/0 - 2/1")
    
    def test_update_kwargs2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(width=1, x=1)
        self.assertEqual(r.__str__(), "[Rectangle] (7) 1/0 - 1/2")

    def test_update_kwargs3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/2")
    
    def test_update_kwargs4(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.__str__(), "[Rectangle] (7) 1/3 - 4/2")
    
    def test_update_kwargs5(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(x=1, height=2, y=3, width=4)
        r.update(id=None, y=1, width=4, x=3)
        self.assertEqual(r.__str__(), f"[Rectangle] ({r.id}) 3/1 - 4/2")
    
    def test_update_kwargs_ErrWidth1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="1")
        
    def test_update_kwargs_ErrWidth2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
    
    def test_update_kwargs_ErrWidth3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-1)
    
    def test_update_kwargs_Errheight1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="1")
        
    def test_update_kwargs_Errheight2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)
    
    def test_update_kwargs_Errheight3(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-1)
    
    def test_update_kwargs_ErrX1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="1")
        
    def test_update_kwargs_ErrX2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    def test_update_kwargs_ErrY1(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="1")
        
    def test_update_kwargs_ErrY2(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)
    
    def test_update_arg_kwargs(self):
        r = Rectangle(2, 2, 2, 0, 7)
        r.update(1, 2, y=3, height=4)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/3 - 2/4")

class TestRectangle_Dict(unittest.TestCase):
    """
    Test case class to validate the to_dictionary method of Rectangle class.
    """
    def test_todict(self):
        r = Rectangle(10, 2, 1, 9, 1)
        dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r.to_dictionary(), dict)
    
    def test_dictErr(self):
        r = Rectangle(2, 2, 2, 0, 7)
        with self.assertRaises(TypeError):
            r.to_dictionary(5)
