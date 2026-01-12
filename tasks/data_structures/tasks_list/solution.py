class ListNode:
    """Элемент линейного связного списка."""
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def display_linked_list(head_node: ListNode) -> None:
    """Выводит все значения связного списка, начиная с головного элемента.
    
    Каждое значение печатается на отдельной строке.
    
    Args:
        head_node: первый элемент списка
        
    Complexity: Time O(n), Space O(1)
    """
    current = head_node
    while current is not None:
        print(current.data)
        current = current.next_node