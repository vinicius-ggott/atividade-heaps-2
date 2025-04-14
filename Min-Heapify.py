def min_heapify(A, i):
    def left(i):
        return 2 * i + 1

    def right(i):
        return 2 * i + 2

    l = left(i)
    r = right(i)
    menor = i
    if l < len(A) and A[l] < A[i]:
        menor = l
    if r < len(A) and A[r] < A[menor]:
        menor = r
    if menor != i:
        A[i], A[menor] = A[menor], A[i]
        min_heapify(A, menor)
