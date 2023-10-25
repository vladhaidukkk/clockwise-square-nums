import unittest
from parameterized import parameterized
from clockwise_square_nums import create_matrix


class TestClockwiseSquareNums(unittest.TestCase):
    @parameterized.expand([
        (1, [[1]]),
        (2, [
            [1, 2],
            [4, 3]
        ]),
        (3, [
            [7, 8, 9],
            [6, 1, 2],
            [5, 4, 3]
        ]),
        (4, [
            [7, 8, 9, 10],
            [6, 1, 2, 11],
            [5, 4, 3, 12],
            [16, 15, 14, 13]
        ]),
        (5, [
            [21, 22, 23, 24, 25],
            [20, 7, 8, 9, 10],
            [19, 6, 1, 2, 11],
            [18, 5, 4, 3, 12],
            [17, 16, 15, 14, 13]
        ]),
    ])
    def test_create_matrix(self, arg, expected):
        self.assertEqual(expected, create_matrix(arg))

    @parameterized.expand([
        (0, ValueError),
        (-1, ValueError),
    ])
    def test_create_matrix_exception(self, arg, expected):
        with self.assertRaises(expected):
            create_matrix(arg)


if __name__ == "__main__":
    unittest.main()
