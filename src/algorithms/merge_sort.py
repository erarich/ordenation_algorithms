
# Programa Python para implementação de MergeSort

# Mescla dois subarrays de arr[].
# O primeiro subarray é arr[l..m]
# O segundo subarray é arr[m+1..r]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # cria arrays temporárias
    L = [0] * (n1)
    R = [0] * (n2)

    # Copia dados para arrays temporários L[] e R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

   # Mesclar os arrays temporários de volta em arr[l..r]
    i = 0  # Índice inicial do primeiro subarray
    j = 0  # Índice inicial do segundo subarray
    k = l  # Índice inicial do subarray mesclado

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copie os elementos restantes de L[], se houver algum
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # # Copie os elementos restantes de L[], se houver algum
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l é para o índice esquerdo e r é o índice direito da submatriz de arr a ser classificada


def merge_sort(arr, l, r):
    if l < r:

        # O mesmo que (l+r)//2, mas evita overflow para l e h grandes
        m = l+(r-l)//2

        # Classifique a primeira e a segunda metades
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


# # Código do driver para testar acima
# arr = [12, 11, 13, 5, 6, 7]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i], end=" ")

# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i], end=" ")
