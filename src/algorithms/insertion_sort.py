
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# # Vetor com 10 elementos
# vetor = [29, 10, 14, 37, 13, 45, 19, 7, 12, 33]

# # Imprimir o vetor não ordenado
# print("Vetor não ordenado:", vetor)

# # Ordenar o vetor usando Insertion Sort
# insertion_sort(vetor)

# # Imprimir o vetor ordenado
# print("Vetor ordenado é:", vetor)
