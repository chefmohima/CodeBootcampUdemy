# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

import pytest


def chunk_array(l, n):
    i = 0
    result = []
    # outer loop iterates over the array
    # inner loop maintains item count for a chunk
    while i in range(len(l)):
        sublist, counter = [], 0
        while counter in range(n) and i < len(l):
            sublist.append(l[i])
            i += 1
            counter += 1
        result.append(sublist)
    return result


def chunk_array_slice(l, n):
    start_index, slice_index = 0, n
    main_list = []
    # using array slice for each chunk
    # increment start, end of the slice by length of chunk
    while slice_index < len(l):
        main_list.append(l[start_index:slice_index])
        start_index += n
        slice_index += n
    # look for leftover elements when the last slice has less than N elements
    if start_index < len(l):
        main_list.append(l[start_index:])
    return main_list




def test_chunk_array():
    assert chunk_array([1, 2, 3, 4], 2) == [[ 1, 2], [3, 4]]


def test_chunk_array_slice():
    assert chunk_array_slice([1, 2, 3, 4, 5], 4) == [[ 1, 2, 3, 4], [5]]
