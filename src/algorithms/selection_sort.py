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

# Test with sorted and random lists
sorted_list = list(range(100000))
random_list = sorted_list.copy()
import random
random.shuffle(random_list)

# Measure time for sorted list
import time
start_time = time.time()
selection_sort(sorted_list)
end_time = time.time()
print("Time for sorted list:", (end_time - start_time) * 1000, "ms")

# Measure time for random list
start_time = time.time()
selection_sort(random_list)
end_time = time.time()
print("Time for random list:", (end_time - start_time) * 1000, "ms")