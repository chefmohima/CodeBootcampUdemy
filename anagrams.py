# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False

import pytest
import re


def anagrams_with_dicts(s1, s2):
    # remove punctuation and spaces
    pattern = re.compile(r"[!,\s]")
    s1 = re.sub(pattern, '', s1)
    s2 = re.sub(pattern, '', s2)
    # convert all chars to lowercase for case insensitive comparisons
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    # count chars in s1 and s2 in 2 dictionaries
    char_map_s1 = {}
    char_map_s2 = {}
    for c in s1:
        if c not in char_map_s1:
            char_map_s1[c] = 1
        else:
            char_map_s1[c] += 1
    for c in s2:
        if c not in char_map_s2:
            char_map_s2[c] = 1
        else:
            char_map_s2[c] += 1
    # compare the 2 dictionaries
    if char_map_s2 != char_map_s1:
        return False
    return True


def anagrams_with_sort(s1,s2):
    pattern = re.compile(r'[!,\s]')
    s1 = re.sub(pattern, '', s1)
    s2 = re.sub(pattern, '', s2)
    s1 = s1.upper()
    s2 = s2.upper()
    # sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)
    # not anagrams if lengths mismatch
    if len(s1) != len(s2):
        return False
    # compare char at each index, if mismatch then not an anagram
    for idx in range(len(s1)):
        if s1[idx] != s2[idx]:
            return False
    return True


def test_is_anagram01():
    assert anagrams_with_dicts('rail safety', 'fairy tales') == True
    assert anagrams_with_dicts('RAIL! SAFETY!', 'fairy tales') == True
    assert anagrams_with_dicts('Hi there', 'Bye there') == False


def test_is_anagram02():
    assert anagrams_with_sort('rail safety', 'fairy tales') == True
    assert anagrams_with_sort('RAIL! SAFETY!', 'fairy tales') == True
    assert anagrams_with_sort('Hi there', 'Bye there') == False


test_is_anagram01()
test_is_anagram02()