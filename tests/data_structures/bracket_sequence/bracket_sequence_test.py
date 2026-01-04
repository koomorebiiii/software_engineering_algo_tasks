from tasks.data_structures.bracket_sequence.solution import is_correct_bracket_seq


def test_correct_sequences():
    """Проверка корректных последовательностей."""
    assert is_correct_bracket_seq("{[()]}") is True
    assert is_correct_bracket_seq("()") is True
    assert is_correct_bracket_seq("") is True
    assert is_correct_bracket_seq("([]){}") is True
    assert is_correct_bracket_seq("((()))[]{}") is True


def test_incorrect_sequences():
    """Проверка некорректных последовательностей."""
    assert is_correct_bracket_seq("{[(]}") is False
    assert is_correct_bracket_seq("([)") is False
    assert is_correct_bracket_seq(")") is False
    assert is_correct_bracket_seq("(") is False
    assert is_correct_bracket_seq("}{") is False


def test_edge_cases():
    """Проверка граничных случаев."""
    assert is_correct_bracket_seq("[]") is True
    assert is_correct_bracket_seq("{}") is True
    assert is_correct_bracket_seq("()[]{}") is True
    assert is_correct_bracket_seq("([{}])") is True
    assert is_correct_bracket_seq("(((") is False