from test_framework import generic_test, test_utils
from collections import defaultdict


def find_anagrams(dictionary):

    sorted_string_to_anagrams = defaultdict(list)
    # DefaultDict: init the dict with default value of the type

    for word in dictionary:
        sorted_string = ''.join(sorted(list(word)))
        sorted_string_to_anagrams[sorted_string].append(word)
        # with the python dict, we have to check if key exists then append word to list. It's easier with DefaultDict

    return [l for l in sorted_string_to_anagrams.values() if len(l) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
