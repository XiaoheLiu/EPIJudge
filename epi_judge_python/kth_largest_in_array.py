from test_framework import generic_test
import random

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.


def find_kth_largest(k, A):

    # 1. In the partition A[left: right+1], pivot around pivot_idx
    # such that larger elements are on the left.
    # Returns the new pivot index after pivoting.
    def partition_around_pivot(pivot_idx, left, right):
        pivot_value = A[pivot_idx]
        # Put pivot on the right
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        new_pivot_idx = left

        # Iterate through [left, right)
        for i in range(left, right):
            if A[i] > pivot_value:
                # if see larger element,
                # swap elements and increment new pivot idx
                A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                new_pivot_idx += 1

        # Put pivot value back into its place
        A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
        return new_pivot_idx

    # 2. Choose random element as pivot and partition around it
    left, right = 0, len(A) - 1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(pivot_idx, left, right)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        # if there are more larger elements, keep searching on the left partition
        if new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
