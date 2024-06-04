def insertion_sort(a):
    comparisons = 0
    swaps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < a[j]:
                a[j + 1] = a[j]
                swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        if j != i - 1:
            swaps += 1  # Para a colocação final da chave
    return a, comparisons, swaps
