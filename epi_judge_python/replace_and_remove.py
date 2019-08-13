import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # 1. forward iteration: remove 'b', count 'a'
    write_idx = a_count = 0

    for i in range(size):
        if s[i] == 'a':
            a_count += 1
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1

    size = write_idx + a_count

    # 2. backward iteration: replace 'a' by 'd','d'
    i = write_idx - 1
    j = size - 1
    while j >= 0:
        if s[i] == 'a':
            s[j], s[j-1] = 'd', 'd'
            j -= 2
        else:
            s[j] = s[i]
            j -= 1
        i -= 1

    return size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
