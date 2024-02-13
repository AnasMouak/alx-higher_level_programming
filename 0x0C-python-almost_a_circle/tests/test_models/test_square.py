#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
import sys
import io

from models.base import Base
from models.square import Square


class TestSquareID_Attr(unittest.TestCase):
    """
    Test cases for the Square class attributes and ID assignment.
    """
    def test_square_is_base(self):
        self.assertIsInstance(Square(3), Base)

    def test_id0(self):
        s1 = Square(3, 4)
        s2 = Square(2, 1)
        s3 = Square(5, 5, 7)
        self.assertEqual(s1.id, s3.id - 2)

    def test_id1(self):
        s1 = Square(1, 2, 1)
        s2 = Square(10, 2, 0)
        self.assertEqual(s1.id, s2.id - 1)

    def test_id2(self):
        self.assertEqual(Square(10, 2, 0, 12).id, 12)

    def test_error_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_error_arg3(self):
        with self.assertRaises(TypeError):
            Square(10, 2, 0, 1, 12)

    def test_Getsize(self):
        self.assertEqual(Square(10, 2, 0, 0).size, 10)

    def test_Getx(self):
        self.assertEqual(Square(10, 2, 0, 0).x, 2)

    def test_Gety(self):
        self.assertEqual(Square(10, 2, 0, 0).y, 0)

    def test_Setsize(self):
        s = Square(10, 2, 0, 0)
        s.size = 4
        self.assertEqual(s.size, 4)

    def test_Getheight(self):
        s = Square(10, 2, 0, 0)
        s.size = 3
        self.assertEqual(s.height, 3)

    def test_Getwidth(self):
        s = Square(10, 2, 0, 0)
        s.size = 3
        self.assertEqual(s.width, 3)

    def test_Setx(self):
        s = Square(10, 2, 0, 0)
        s.x = 3
        self.assertEqual(s.x, 3)

    def test_Sety(self):
        s = Square(10, 2, 0, 0)
        s.y = 3
        self.assertEqual(s.y, 3)

    def test_prvAttr_size(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 0, 0).__size

    def test_prvAttr_width(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 0, 0).__width

    def test_prvAttr_height(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 0, 0).__height

    def test_prvAttr_x(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 0, 0).__x

    def test_prvAttr_y(self):
        with self.assertRaises(AttributeError):
            Square(10, 2, 0, 0).__y


class TestSquareType_ValueError(unittest.TestCase):
    """
    Test cases for verifying error handling in the Square class constructor.
    """
    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.1)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"10": 1, "11": 2})

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_none_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "2")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, -1.1)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2, 3])

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2, 3))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"10": 1, "11": 2})

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2, 3})

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 1, "2")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, -1.1)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, (1, 2, 3))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 11, {"10": 1, "11": 2})

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, {1, 2, 3})

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 2, None)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -2)

    def test_sizeErr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("-1", "2")

    def test_widthErr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1", 2, -1.1)

    def test_xErr(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "-3", [1, 2, 3])

    def test_sizeErr2(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2, 2, (1, 2, 3))

    def test_sizeErr2(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, {"10": 1, "11": 2})

    def test_xErr2(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2, -1)


class TestSquare_Area(unittest.TestCase):
    """
    Test case class to validate the area method of Square class.
    """
    def test_area(self):
        self.assertEqual(Square(2).area(), 4)

    def test_area1(self):
        self.assertEqual(Square(3, 2, 3, 4).area(), 9)

    def test_area2(self):
        s = Square(3, 2, 3, 4)
        s.size = 6
        self.assertEqual(s.area(), 36)

    def test_area3(self):
        s = Square(3, 2, 3, 4)
        s.width = 6
        self.assertEqual(s.area(), 18)

    def test_areaErr(self):
        s = Square(1, 2, 2, 1)
        with self.assertRaises(TypeError):
            s.area(4)


class TestSquare_Display(unittest.TestCase):
    """
    Test case class to validate the display method of Square class.
    """
    @staticmethod
    def display_stdout(square):
        """Captures and returns text printed to stdout.

        Args:
            rect (Square): The Square to print to stdout.
        Returns:
            The text printed to stdout .
        """
        display = io.StringIO()
        sys.stdout = display
        square.display()
        sys.stdout = sys.__stdout__
        return display

    def test_display1(self):
        s = Square(2)
        display = TestSquare_Display.display_stdout(s)
        self.assertEqual(display.getvalue(), "##\n##\n")

    def test_display2(self):
        s = Square(4)
        display = TestSquare_Display.display_stdout(s)
        self.assertEqual(display.getvalue(), "####\n####\n####\n####\n")

    def test_displayErr(self):
        s = Square(1, 2, 2, 1)
        with self.assertRaises(TypeError):
            s.display(4)

    def test_display_with_position1(self):
        s = Square(2, 1, 1)
        display = TestSquare_Display.display_stdout(s)
        self.assertEqual(display.getvalue(), "\n ##\n ##\n")

    def test_display_with_position2(self):
        s = Square(2, 2, 0)
        display = TestSquare_Display.display_stdout(s)
        self.assertEqual(display.getvalue(), "  ##\n  ##\n")

    def test_display_with_position3(self):
        s = Square(4, 0, 2)
        display = TestSquare_Display.display_stdout(s)
        self.assertEqual(display.getvalue(), "\n\n####\n####\n####\n####\n")


class TestSquare_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Square class.
    """
    def test_str1(self):
        s = Square(3)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 0/0 - 3")

    def test_str11(self):
        s = Square(2, 2, 2)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 2/2 - 2")

    def test_str2(self):
        s = Square(2, 2)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 2/0 - 2")

    def test_str3(self):
        s = Square(2, 2, 2, 4)
        self.assertEqual(s.__str__(), f"[Square] (4) 2/2 - 2")

    def test_str4(self):
        s = Square(2, 2, 2, (1, 4))
        s.size = 4
        s.x = 1
        s.y = 1
        self.assertEqual(s.__str__(), f"[Square] ((1, 4)) 1/1 - 4")

    def test_strErr(self):
        s = Square(1, 2, 2, 1)
        with self.assertRaises(TypeError):
            s.__str__(4)


class TestSquare_Update(unittest.TestCase):
    """
    Test case class to validate the update method of Square class.
    """
    def test_update1(self):
        s = Square(2, 2, 2, 7)
        s.update(2)
        self.assertEqual(s.__str__(), "[Square] (2) 2/2 - 2")

    def test_update2(self):
        s = Square(2, 2, 2, 7)
        s.update(2, 6)
        self.assertEqual(s.__str__(), "[Square] (2) 2/2 - 6")

    def test_update3(self):
        s = Square(2, 2, 2, 7)
        s.update(2, 6, 2)
        self.assertEqual(s.__str__(), "[Square] (2) 2/2 - 6")

    def test_update4(self):
        s = Square(2, 2, 2, 7)
        s.update(2, 6, 2, 1)
        self.assertEqual(s.__str__(), "[Square] (2) 2/1 - 6")

    def test_update5(self):
        s = Square(2, 2, 2, 7)
        s.update(2, 6, 9, 1)
        s.update(3, 5, 3, 1)
        self.assertEqual(s.__str__(), "[Square] (3) 3/1 - 5")

    def test_update6(self):
        s = Square(2, 2, 2, 7)
        s.update(2, 6, 9, 1)
        s.update(None, 3, 1, 1)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 1/1 - 3")

    def test_updateErrsize1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(4, "1")

    def test_updateErrsize2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(4, 0)

    def test_updateErrsize3(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(4, -1)

    def test_updateErrX1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(4, 2, "1")

    def test_updateErrX2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(4, 2, -1)

    def test_updateErrY1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(4, 2, 2, "1")

    def test_updateErrY2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(4, 2, 2, -1)

    def test_update_kwargs1(self):
        s = Square(1, 2, 2, 7)
        s.update(size=2)
        self.assertEqual(s.__str__(), "[Square] (7) 2/2 - 2")

    def test_update_kwargs2(self):
        s = Square(2, 2, 2, 7)
        s.update(y=1, x=1)
        self.assertEqual(s.__str__(), "[Square] (7) 1/1 - 2")

    def test_update_kwargs3(self):
        s = Square(2, 2, 2, 7)
        s.update(y=1, size=3, x=3, id=89)
        self.assertEqual(s.__str__(), "[Square] (89) 3/1 - 3")

    def test_update_kwargs4(self):
        s = Square(2, 2, 2, 7)
        s.update(x=1, height=2, y=3, size=4)
        self.assertEqual(s.__str__(), "[Square] (7) 1/3 - 4")

    def test_update_kwargs5(self):
        s = Square(2, 2, 2, 7)
        s.update(x=1, y=3, size=4)
        s.update(id=None, y=1, size=4, x=3)
        self.assertEqual(s.__str__(), f"[Square] ({s.id}) 3/1 - 4")

    def test_update_kwargs_ErrSize1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="1")

    def test_update_kwargs_ErrSize2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_ErrSize3(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-1)

    def test_update_kwargs_ErrX1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="1")

    def test_update_kwargs_ErrX2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-1)

    def test_update_kwargs_ErrY1(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="1")

    def test_update_kwargs_ErrY2(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-1)

    def test_update_arg_kwargs(self):
        s = Square(2, 2, 2, 7)
        s.update(1, 3, y=3, x=1)
        self.assertEqual(s.__str__(), "[Square] (1) 1/3 - 3")


class TestSquare_Dict(unittest.TestCase):
    """
    Test case class to validate the to_dictionary method of Square class.
    """
    def test_todict(self):
        s = Square(10, 2, 1, 1)
        dict = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertDictEqual(s.to_dictionary(), dict)

    def test_dictErr(self):
        s = Square(2, 2, 2, 7)
        with self.assertRaises(TypeError):
            s.to_dictionary(5)
