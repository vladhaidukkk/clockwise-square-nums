import unittest
from parameterized import parameterized
from clockwise_square_nums_cli import create_parser


class TestCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = create_parser()

    @parameterized.expand([
        (["5"], 5, 4),
        (["5", "--width", "6"], 5, 6),
    ])
    def test_parser(self, input_args, side, width):
        args = self.parser.parse_args(input_args)
        self.assertEqual(side, args.side)
        self.assertEqual(width, args.width)


if __name__ == "__main__":
    unittest.main()
