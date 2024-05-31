def merge_sort(arr):
    comparisons = 0
    swaps = 0

    def merge(left, right):
        nonlocal comparisons, swaps
        merged = []
        l = r = 0
        while l < len(left) and r < len(right):
            comparisons += 1
            if left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        merged.extend(left[l:])
        merged.extend(right[r:])
        return merged

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, comparisons, swaps

# Test with sorted and random lists
sorted_list = list(range(100000))
random_list = sorted_list.copy()
import random
random.shuffle(random_list)

# Measure time for sorted list
import time
start_time = time.time()
merge_sort(sorted_list)
end_time = time.time()
print("Time for sorted list:", (end_time - start_time) * 1000, "ms")

# Measure time for random list
start_time = time.time()
merge_sort(random_list)
end_time = time.time()
print("Time for random list:", (end_time - start_time) * 1000, "ms")