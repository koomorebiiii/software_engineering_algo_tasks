import pytest
from tasks.recursion.binary_search.solution import locate_element

def test_element_found_with_duplicates():
    """Поиск в массиве с повторяющимися элементами."""
    data = [1, 2, 2, 4, 7]
    result = locate_element(data, 2)
    assert result == 1 or result == 2 

def test_element_not_present():
    """Поиск отсутствующего элемента."""
    data = [1, 3, 5]
    assert locate_element(data, 2) == -1

def test_empty_collection():
    """Поиск в пустой коллекции."""
    assert locate_element([], 10) == -1

def test_single_element_exists():
    """Поиск единственного элемента (найден)."""
    assert locate_element([5], 5) == 0

def test_single_element_missing():
    """Поиск в коллекции из одного элемента (не найден)."""
    assert locate_element([5], 10) == -1

def test_first_position():
    """Поиск элемента в начале массива."""
    data = [1, 2, 3, 4, 5]
    assert locate_element(data, 1) == 0

def test_last_position():
    """Поиск элемента в конце массива."""
    data = [1, 2, 3, 4, 5]
    assert locate_element(data, 5) == 4

def test_large_dataset():
    """Проверка производительности на большом наборе данных."""
    large_data = list(range(1_000_000))
    assert locate_element(large_data, 999_999) == 999_999
    assert locate_element(large_data, -5) == -1

def test_negative_numbers():
    """Поиск отрицательных значений."""
    data = [-10, -5, 0, 3, 7]
    assert locate_element(data, -5) == 1
    assert locate_element(data, -15) == -1

def test_extreme_values():
    """Поиск значений на границах допустимого диапазона."""
    data = [-1_000_000_000, -500, 0, 500, 1_000_000_000]
    assert locate_element(data, 1_000_000_000) == 4