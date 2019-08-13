from test_framework import generic_test


def square_root(k):
    # find largest x where x*x <= k

    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        sqr = mid * mid
        if sqr > k:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
