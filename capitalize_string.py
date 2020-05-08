# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'


import pytest


def capitalize_string(s):
    result = ''
    # get words
    words = s.split()
    # lowercase each word
    word_list = [word.lower() for word in words]
    for word in word_list:
        # uppercase first letter of each word and append to result string along with space
        word = word[0].upper() + word[1:]
        result += word+' '
    # remove trailing space
    return result.strip()


def test_capitalize_string():
    assert capitalize_string('look, it is working!') == 'Look, It Is Working!'
    assert capitalize_string('a lazy fox') == 'A Lazy Fox'
    assert capitalize_string('look, it is working!') == 'Look, It Is Working!'


