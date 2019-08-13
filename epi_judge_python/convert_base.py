from test_framework import generic_test
from string import hexdigits
from functools import reduce

# Note:
# string.hexdigits
# >> '0123456789abcdefABCDEF'


def convert_base(num_as_string, b1, b2):

    # 1. convert to base 10 number
    is_negative = False
    if num_as_string[0] == '-':
        is_negative, num_as_string = True, num_as_string[1:]

    base_10_num = reduce(
        lambda x, c: x * b1 + hexdigits.index(c.lower()),
        num_as_string,
        0
    )

    # 2. Convert base_10_num to base b2 num string
    # Iterative Approach:
    # s = []
    # while True:
    #     s.append(hexdigits[base_10_num % b2].upper())
    #     base_10_num //= b2
    #     if base_10_num == 0:
    #         break
    # return ('-' if is_negative else '') + ''.join(reversed(s))

    # Recursive Approach:
    def convert_positive_num_to_b2_str(num, b2):
        if num == 0:
            return ''
        return convert_positive_num_to_b2_str(num//b2, b2) + hexdigits[num % b2].upper()

    return ('-' if is_negative else '') + ('0' if base_10_num == 0 else convert_positive_num_to_b2_str(base_10_num, b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
