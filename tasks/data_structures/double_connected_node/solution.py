class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    """Разворачивает двусвязный список.

    Args:
        node: голова списка

    Returns:
        новая голова (последний элемент)

    Time: O(n), Space: O(1)
    """
    if not node:
        return node
    curr = node
    new_head = node
    while curr:
        curr.next, curr.prev = curr.prev, curr.next
        new_head = curr
        curr = curr.prev
    return new_head