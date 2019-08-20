from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    result = []
    pa, pb = 0, 0
    while pa < len(A) and pb < len(B):
        a, b = A[pa], B[pb]
        if a == b:
            if len(result) == 0 or result[-1] != a:
                result.append(a)
            pa += 1
            pb += 1
        elif a > b:
            pb += 1
        else:
            pa += 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
