import argparse
from clockwise_square_nums import create_matrix


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "side",
        type=int,
        help="size of the side in the printed square"
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=4,
        help="width of each number in the printed square (default: 4)"
    )
    return parser


def print_matrix(matrix, *, width=4):
    for row in matrix:
        for col in row:
            print(f"{col}".rjust(width), end=" ")
        print()


def main():
    parser = create_parser()
    args = parser.parse_args()
    matrix = create_matrix(args.side)
    print_matrix(matrix, width=args.width)


if __name__ == "__main__":
    main()
