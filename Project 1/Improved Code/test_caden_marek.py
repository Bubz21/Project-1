import unittest
from caden_marek_area import *


# Class for testing the math module
class MyTestCase(unittest.TestCase):
    # Test the area of a circle and tests for errors
    def test_area_circle(self):
        self.assertEqual(area_circle(10), 314.1592653589793)  # add assertion here
        self.assertAlmostEqual(area_circle(0.1), 0.01, delta=0.04)

        with self.assertRaises(TypeError):
            area_circle('7.5')

        with self.assertRaises(ValueError):
            area_circle(0)
            area_circle(-3)

    # Test the area of a rectangle and tests for errors
    def test_area_rectangle(self):
        self.assertEqual(area_rectangle(2, 1), 2)
        self.assertAlmostEqual(area_rectangle(1.5, 1), 1.5, delta=0.001)
        self.assertAlmostEqual(area_rectangle(1, 1.6), 1.6, delta=0.001)
        self.assertAlmostEqual(area_rectangle(1.5, 2.1), 3.15, delta=0.001)

        with self.assertRaises(TypeError):
            area_rectangle('7.5', 1)
            area_rectangle(1, '7.5')
            area_rectangle('7.5', '1')

        with self.assertRaises(ValueError):
            area_rectangle(0, 1)
            area_rectangle(1, 0)
            area_rectangle(0, 0)
            area_rectangle(-1, 2)
            area_rectangle(2, -1)
            area_rectangle(-3, -1)

    # Test the area of a square and tests for errors
    def test_area_square(self):
        self.assertEqual(area_square(10), 100)  # add assertion here
        self.assertAlmostEqual(area_square(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            area_square('7.5')

        with self.assertRaises(ValueError):
            area_square(0)
            area_square(-3)

    # Test the area of a triangle and tests for errors
    def test_area_triangle(self):
        self.assertEqual(area_triangle(2, 1), 1)
        self.assertAlmostEqual(area_triangle(1.5, 1), 0.75, delta=0.001)
        self.assertAlmostEqual(area_triangle(1, 1.6), 0.8, delta=0.001)
        self.assertAlmostEqual(area_triangle(1.5, 2.1), 1.575, delta=0.001)

        with self.assertRaises(TypeError):
            area_triangle('7.5', 1)
            area_triangle(1, '7.5')
            area_triangle('7.5', '1')

        with self.assertRaises(ValueError):
            area_triangle(0, 1)
            area_triangle(1, 0)
            area_triangle(0, 0)
            area_triangle(-1, 2)
            area_triangle(2, -1)
            area_triangle(-3, -1)


if __name__ == '__main__':
    unittest.main()
