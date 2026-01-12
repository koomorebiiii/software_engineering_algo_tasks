import pytest
from tasks.data_structures.tasks_list.solution import ListNode, display_linked_list


def test_output_four_elements(capsys):
    """Вывод списка из четырёх элементов."""
    tail = ListNode("четвёртый")
    third = ListNode("третий", tail)
    second = ListNode("второй", third)
    head = ListNode("первый", second)
    
    display_linked_list(head)
    captured = capsys.readouterr()
    expected = "первый\nвторой\nтретий\nчетвёртый\n"
    assert captured.out == expected


def test_single_element_list(capsys):
    """Вывод списка из одного элемента."""
    single_node = ListNode(42)
    
    display_linked_list(single_node)
    captured = capsys.readouterr()
    assert captured.out == "42\n"


def test_numeric_values(capsys):
    """Вывод списка с числовыми значениями."""
    node2 = ListNode(30.5)
    node1 = ListNode(20, node2)
    head = ListNode(10, node1)
    
    display_linked_list(head)
    captured = capsys.readouterr()
    expected = "10\n20\n30.5\n"
    assert captured.out == expected


def test_mixed_data_types(capsys):
    """Вывод списка с элементами разных типов."""
    node3 = ListNode([1, 2, 3])
    node2 = ListNode(True, node3)
    node1 = ListNode("строка", node2)
    head = ListNode(100, node1)
    
    display_linked_list(head)
    captured = capsys.readouterr()
    expected = "100\nстрока\nTrue\n[1, 2, 3]\n"
    assert captured.out == expected


def test_maximum_size_list(capsys):
    """Проверка вывода списка максимально допустимой длины."""
    current = ListNode(0)
    head = current
    
    for i in range(1, 5000):
        current.next_node = ListNode(i)
        current = current.next_node
    
    display_linked_list(head)
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    
    assert len(lines) == 5000
    assert lines[0] == "0"
    assert lines[4999] == "4999"
    assert lines[2500] == "2500"  


def test_list_with_empty_strings(capsys):
    """Вывод списка, содержащего пустые строки."""
    node2 = ListNode("")
    node1 = ListNode("непустой", node2)
    head = ListNode("", node1)
    
    display_linked_list(head)
    captured = capsys.readouterr()
    expected = "\nнепустой\n\n"
    assert captured.out == expected


@pytest.mark.parametrize("count", [1, 2, 3, 5, 10])
def test_various_lengths_parametrized(capsys, count):
    """Параметризованный тест для списков разной длины."""
    current = ListNode(f"элемент_{count-1}")
    
    for i in range(count-2, -1, -1):
        current = ListNode(f"элемент_{i}", current)
    
    head = current
    
    display_linked_list(head)
    captured = capsys.readouterr()
    
    lines = captured.out.strip().split('\n')
    assert len(lines) == count
    
    for i in range(count):
        assert lines[i] == f"элемент_{i}"