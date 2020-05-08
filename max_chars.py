
# --- Directions
# Given a string, return the character that is most
# commonly used in the string.
# --- Examples
# maxChar("abcccccccd") === "c"
# maxChar("apple 1231111") === "1"

import pytest


def max_char(s):
    max_count, max_char = 0, None
    char_counter = {}
    for c in s:
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1
        if char_counter[c] > max_count:
            max_count, max_char = char_counter[c], c
    return max_char




def test_max_char_letters():
    assert max_char("abcccccccd") == "c"


def test_max_char_numbers():
    assert max_char("apple 1231111") == "1"




