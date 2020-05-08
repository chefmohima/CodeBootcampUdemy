# --- Directions
# Given a string, return a new string with the reversed
# order of characters
# --- Examples
#   reverse('apple') === 'leppa'
#   reverse('hello') === 'olleh'
#   reverse('Greetings!') === '!sgniteerG'

import pytest


def reverse_string_01(s):
    # convert to list,
    # swap chars from start to end
    # join list to string and return
    s = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return ''.join(s)


def reverse_string_02(s):
    # initialise an empty result string
    # iterate from last to first index of input string and
    # append char to new string
    new_string = ''
    for idx in range(len(s), -1, -1):
        new_string += s[idx]
    return new_string


def reverse_string_03(s):
    # using slice notation
    return s[::-1]


def test_reverse_string_odd_chars():
    assert reverse_string_01('apple') == 'elppa'
    assert reverse_string_01('hello') == 'olleh'


def test_reverse_string_spl_chars():
    assert reverse_string_01('Greetings!') == '!sgniteerG'


def test_reverse_string_empty_string():
    assert reverse_string_01('') == ''


test_reverse_string_odd_chars()
test_reverse_string_spl_chars()
test_reverse_string_empty_string()


