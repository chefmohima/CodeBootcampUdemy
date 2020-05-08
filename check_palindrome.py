# --- Directions
# Given a string, return true if the string is a palindrome
# or false if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("abba") === true
#   palindrome("abcdefg") === false
import pytest


def check_palindrome_01(s):
    if s == s[::-1]:
        return True
    return False


def check_palindrome_02(s):
    start, end = 0, len(s)-1
    while start<end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def test_check_palindrome_even_letters():
    assert check_palindrome_02('abba') == True


def test_check_palindrome_odd_letters():
    assert check_palindrome_02('radar') == True


def test_check_palindrome_empty_string():
    assert check_palindrome_02('') == True


def test_check_not_a_palindrome():
    assert check_palindrome_02('abcdefg') == False


test_check_palindrome_even_letters()
test_check_palindrome_odd_letters()
test_check_palindrome_empty_string()




