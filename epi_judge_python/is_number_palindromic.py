from test_framework import generic_test


def is_palindrome_number(x):
    s = str(x)
    return all([s[i] == s[~i] for i in range(len(s)//2)])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
