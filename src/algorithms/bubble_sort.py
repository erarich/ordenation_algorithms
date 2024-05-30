
def bubble_sort(a):
    n = len(a)
    for j in range(n - 1, 0, -1):
        for k in range(j):
            if a[k + 1] < a[k]:
                a[k], a[k + 1] = a[k + 1], a[k]


# # Exemplo de uso:
# vetor = [64, 34, 25, 12, 22, 11, 90]

# # Ordenar o vetor usando Bubble Sort
# bubble_sort(vetor)

# # Imprimir o vetor ordenado
# print("Vetor ordenado é:", vetor)
