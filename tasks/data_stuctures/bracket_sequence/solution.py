def is_correct_bracket_seq(sequence: str) -> bool:
    """Проверяет, является ли строка правильной скобочной последовательностью.

    Args:
        sequence: строка, содержащая только символы ()[]{}

    Returns:
        True если последовательность правильная, иначе False

    Time: O(n), Space: O(n)
    """
    if not sequence:
        return True

    closing_to_opening = {')': '(', ']': '[', '}': '{'}
    opening_set = {'(', '[', '{'}

    stack = []

    for bracket in sequence:
        if bracket in opening_set:
            stack.append(bracket)
        elif bracket in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[bracket]:
                return False
        # По условию задачи других символов не должно быть

    return not stack
