from test_framework import generic_test
import math


def square_root(x):
    left, right = (0.0, x) if x > 1.0 else (0.0, 1.0)

    while not math.isclose(left, right):
        mid = (left + right)/2.0
        sqr = mid * mid
        if sqr > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
