from test_framework import generic_test
from test_framework.test_failure import TestFailure
from functools import reduce

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        c = chr(ord('0') + x % 10)
        s.append(c)
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    digits = '0123456789'

    is_negative = False
    if s[0] == '-':
        is_negative, s = True, s[1:]

    # result = 0
    # for c in s:
    #     result = result * 10 + digits.index(c)

    result = reduce(
        lambda acc, c: acc * 10 + digits.index(c),
        s,
        0)

    return result * (-1 if is_negative else 1)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
