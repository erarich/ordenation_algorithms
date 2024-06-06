def selection_sort(arr):
    comparisons = 0
    swaps = 0

    def swap(i, j):
        nonlocal swaps
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        swap(i, min_index)

    return arr, comparisons, swaps
