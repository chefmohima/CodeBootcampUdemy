# --- Directions
# Given an integer, return an integer that is the reverse
# ordering of numbers.
# --- Examples
#   reverseInt(15) === 51
#   reverseInt(981) === 189
#   reverseInt(500) === 5
#   reverseInt(-15) === -51
#   reverseInt(-90) === -9

import pytest


def reverse_int(num):
    digits, negative = [], False
    if num < 0:
        negative = True
        # consider number positive for calculation purposes and add sign at the end
        num = -num
    while num > 10:
        digits.append(num % 10)
        num = num // 10
    digits.append(num)
    digits = list(reversed(digits))
    print(digits)
    result = 0
    for idx in range(len(digits)):
        result += digits[idx]*(10**idx)
    if negative:
        return -result
    return result


def test_reverse_int_positive():
    assert reverse_int(15) == 51


def test_reverse_int_negative():
    assert reverse_int(-51) == -15


def test_reverse_int_trailing_zero():
    assert  reverse_int(500) == 5






