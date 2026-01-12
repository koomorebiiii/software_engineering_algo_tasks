def locate_element(sorted_collection: list[int], search_value: int) -> int:
    """Осуществляет бинарный поиск в упорядоченной коллекции.
    
    Returns:
        индекс элемента или -1 при отсутствии.
    """
    start_idx, end_idx = 0, len(sorted_collection) - 1
    
    while start_idx <= end_idx:
        center_idx = (start_idx + end_idx) // 2
        current_value = sorted_collection[center_idx]
        
        if current_value == search_value:
            return center_idx
        elif current_value < search_value:
            start_idx = center_idx + 1
        else:
            end_idx = center_idx - 1
    
    return -1