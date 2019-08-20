from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):

    write_index = m + n - 1
    pa, pb = m - 1, n - 1

    while write_index >= 0 and pb >= 0 and pa >= 0:
        a, b = A[pa], B[pb]
        if b >= a:
            A[write_index] = b
            pb -= 1
        else:
            A[write_index] = a
            pa -= 1
        write_index -= 1

    while pb >= 0:
        A[write_index] = B[pb]
        pb -= 1
        write_index -= 1
        


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
