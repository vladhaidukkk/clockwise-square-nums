# Clockwise Square Numbers

The Clockwise Square Numbers Python program is designed to create a square matrix and fill it with numbers in a clockwise direction (starting from the middle of the square). It offers a visual representation of the numbers, where the numbers are arranged in a clockwise spiral.

## Installation

To install the Clockwise Square Numbers, you will need to have Python and pip installed on your system. Run this command:

```shell
pip install -i https://test.pypi.org/simple/ clockwise-square-nums
```

_It is important to note that this package is published on TestPyPI._

## Usage

The Clockwise Square Numbers provides you with a package as well as a CLI.

### Package Usage

To use the package import `clockwise_square_nums`. Right now it has a single function `create_matrix`:

```shell
from clockwise_square_nums import create_matrix

matrix = create_matrix(3)
assert matrix == [
    [7, 8, 9],
    [6, 1, 2],
    [5, 4, 3],
]
```

### CLI Usage

To use the CLI, use the following command:
```shell
clockwise_square_nums 3
```

To change the width of each number in the printed square, specify the `--width` option:
```shell
clockwise_square_nums 10 --width 5
```

To see all options, use the following command:
```shell
clockwise_square_nums --help
```

## Examples

```shell
$ clockwise_square_nums 3
   7    8    9
   6    1    2
   5    4    3
```

```shell
$ clockwise_square_nums 4 --width 6
     7      8      9     10
     6      1      2     11
     5      4      3     12
    16     15     14     13
```
