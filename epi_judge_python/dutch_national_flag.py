from __future__ import annotations
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    p = A[pivot_index]
    METHOD = 2

    if METHOD == 1:
        # Method 1: O(n) time, O(1) space
        # 1st: pivot <= items to the left, > items to the right
        i, j = 0, len(A)
        while i < j:
            if A[i] <= p:
                i += 1
            else:
                j -= 1
                A[i], A[j] = A[j], A[i]

        # 2nd: in the <= items subarray, pivot < items to the right
        # = items to the right.
        i = 0
        while i < j:
            if A[i] < p:
                i += 1
            else:
                j -= 1
                A[i], A[j] = A[j], A[i]

    else:
        # Method 2: Similar idea but pivot everything in one round
        i, j, k = 0, 0, len(A)  # pointers for <, =, > items
        while j < k:
            if A[j] == p:
                j += 1
            elif A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
            else:
                k -= 1
                A[k], A[j] = A[j], A[k]

    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
    # idx = 52
    # A = [0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 2, 2, 1, 0, 2, 0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2,
    #      1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 1, 2]
    # print(A[52])
    # dutch_flag_partition(idx, A)
    # print(A)
