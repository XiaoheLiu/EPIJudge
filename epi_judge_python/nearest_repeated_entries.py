from test_framework import generic_test


def find_nearest_repetition(paragraph):
    nearest_repetition = float('inf')
    word_to_index = {}

    for i, word in enumerate(paragraph):
        if word in word_to_index:
            nearest_repetition = min(
                nearest_repetition, i - word_to_index[word])
        word_to_index[word] = i

    if nearest_repetition == float('inf'):
        return -1
    return nearest_repetition


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
