from test_framework import generic_test


def parity(x: int) -> int:
    result = 0

    # Explicit Version:
    # while x:
    #     if x & 1:
    #         result += 1
    #     x >>= 1
    # return result % 2

    # Advanced Version
    while x:
        result ^= (x & 1)
        x >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
