from test_framework import generic_test
from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    char_in_letter_counts = Counter(letter_text)

    # ==== Naive method: ====
    # char_in_magazine_counts = Counter(magazine_text)

    # for key in char_in_letter_counts:
    #     if char_in_magazine_counts.get(key) is None or char_in_magazine_counts[key] < char_in_letter_counts[key]:
    #         return False

    # return True

    # === Pythonic Naive method: ===
    # return not (Counter(letter_text) - Counter(magazine_text))

    # ==== More efficient method: ====
    for c in magazine_text:
        if char_in_letter_counts.get(c):
            char_in_letter_counts[c] -= 1
            if char_in_letter_counts[c] == 0:
                del char_in_letter_counts[c]
                if not char_in_letter_counts:
                    return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
