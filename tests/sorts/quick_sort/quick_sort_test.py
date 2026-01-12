import pytest

from tasks.sorts.quick_sort.solution import quick_sort

def test_empty_array():
    assert quick_sort([]) == []

def test_single_element():
    assert quick_sort([3]) == [3]

def test_random_array():
    assert quick_sort([3, 7, 9, 4, 3, 1, 8, 5]) == [1, 3, 3, 4, 5, 7, 8, 9]

def test_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_with_negatives_and_duplicates():
    assert quick_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]

def test_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mixed():
    assert quick_sort([-10, 10, 0]) == [-10, 0, 10]

def test_all_equal():
    assert quick_sort([5] * 50) == [5] * 50