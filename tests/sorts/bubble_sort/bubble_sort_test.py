import pytest

from tasks.sorts.bubble_sort.solution import bubble_sort

def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [[1, 2, 3]]

def test_reverse_sorted():
    assert bubble_sort([3, 2, 1]) == [[2, 1, 3], [1, 2, 3]]

def test_negative_numbers():
    assert bubble_sort([7, -2, -1]) == [[-2, -1, 7]]

def test_long_reverse():
    assert bubble_sort([5, 4, 3, 2, 1]) == [[4, 3, 2, 1, 5], [3, 2, 1, 4, 5], [2, 1, 3, 4, 5], [1, 2, 3, 4, 5]]

def test_empty_array():
    assert bubble_sort([]) == [[]]

def test_single_element():
    assert bubble_sort([1]) == [[1]]

def test_all_equal():
    assert bubble_sort([2, 2, 2]) == [[2, 2, 2]]

def test_two_elements():
    assert bubble_sort([10, 5]) == [[5, 10]]