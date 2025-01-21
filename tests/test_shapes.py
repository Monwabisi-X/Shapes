import unittest
from shapes import (solid_rectangle, hollow_rectangle, right_angled_triangle,
                    inverted_right_angled_triangle, pyramid, inverted_pyramid,
                    diamond, hollow_diamond, number_triangle, floyds_triangle,
                    alphabet_pyramid, mirrored_right_angled_triangle, hourglass,
                    pascals_triangle, diamond_number_pattern)

class TestShapes(unittest.TestCase):
    def test_solid_rectangle(self):
        expected = [
            "******",
            "******",
            "******",
            "******",
        ]
        self.assertEqual(solid_rectangle(4, 6), expected)

    def test_hollow_rectangle(self):
        expected = [
            "******",
            "*    *",
            "*    *",
            "******",
        ]
        self.assertEqual(hollow_rectangle(4, 6), expected)

    def test_right_angled_triangle(self):
        expected = [
            "*",
            "**",
            "***",
            "****",
            "*****",
        ]
        self.assertEqual(right_angled_triangle(5), expected)

    def test_inverted_right_angled_triangle(self):
        expected = [
            "*****",
            "****",
            "***",
            "**",
            "*",
        ]
        self.assertEqual(inverted_right_angled_triangle(5), expected)

    def test_pyramid(self):
        expected = [
            "    *",
            "   ***",
            "  *****",
            " *******",
            "*********",
        ]
        self.assertEqual(pyramid(5), expected)

    def test_inverted_pyramid(self):
        expected = [
            "*********",
            " *******",
            "  *****",
            "   ***",
            "    *",
        ]
        self.assertEqual(inverted_pyramid(5), expected)

    def test_diamond(self):
        expected = [
            "    *",
            "   ***",
            "  *****",
            " *******",
            "*********",
            " *******",
            "  *****",
            "   ***",
            "    *",
        ]
        self.assertEqual(diamond(5), expected)

    def test_hollow_diamond(self):
        expected = [
            "    *",
            "   * *",
            "  *   *",
            " *     *",
            "*       *",
            " *     *",
            "  *   *",
            "   * *",
            "    *",
        ]
        self.assertEqual(hollow_diamond(5), expected)

    def test_number_triangle(self):
        expected = [
            "1",
            "2 2",
            "3 3 3",
            "4 4 4 4",
            "5 5 5 5 5",
        ]
        self.assertEqual(number_triangle(5), expected)

    def test_floyds_triangle(self):
        expected = [
            "1",
            "2 3",
            "4 5 6",
            "7 8 9 10",
            "11 12 13 14 15",
        ]
        self.assertEqual(floyds_triangle(5), expected)

    def test_alphabet_pyramid(self):
        expected = [
            "    A",
            "   A B",
            "  A B C",
            " A B C D",
            "A B C D E",
        ]
        self.assertEqual(alphabet_pyramid(5), expected)

    def test_mirrored_right_angled_triangle(self):
        expected = [
            "    *",
            "   **",
            "  ***",
            " ****",
            "*****",
        ]
        self.assertEqual(mirrored_right_angled_triangle(5), expected)

    def test_hourglass(self):
        expected = [
            "*****",
            " *** ",
            "  *  ",
            " *** ",
            "*****",
        ]
        self.assertEqual(hourglass(5), expected)

    def test_pascals_triangle(self):
        expected = [
            "    1",
            "   1 1",
            "  1 2 1",
            " 1 3 3 1",
            "1 4 6 4 1",
        ]
        self.assertEqual(pascals_triangle(5), expected)

    def test_diamond_number_pattern(self):
        expected = [
            "    1",
            "   121",
            "  12321",
            " 1234321",
            "123454321",
            " 1234321",
            "  12321",
            "   121",
            "    1",
        ]
        self.assertEqual(diamond_number_pattern(5), expected)

if __name__ == "__main__":
    unittest.main()
