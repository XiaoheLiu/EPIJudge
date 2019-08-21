from test_framework import generic_test


def gcd(x, y):
    ## Assuming x, y can be any order
    # if x * y == 0:
    #     return x + y
    # x, y = min(x, y), max(x, y)
    # return gcd(x, (y - x) % x)

    ## Assuming x >= y
    return x if y == 0 else gcd(y, (x-y) % y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
