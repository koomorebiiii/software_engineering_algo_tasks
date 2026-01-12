def bubble_sort(arr: list[int]) -> list[list[int]]:
    """Сортировка пузырьком с промежуточными состояниями.

    Returns:
        Список состояний после каждого прохода с обменами.
    """
    results = []
    n = len(arr)
    arr = arr[:]
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped:
            results.append(arr[:])
    if not results:
        results.append(arr[:])
    return results