def iterative_max_heapify(A, i):
    while i < len(A):
        l = 2 * i + 1  # Left child index
        r = 2 * i + 2  # Right child index
        maior = i

        if l < len(A) and A[l] > A[maior]:
            maior = l
        if r < len(A) and A[r] > A[maior]:
            maior = r

        if maior == i:
            break
        A[i], A[maior] = A[maior], A[i]  # Swap elements
        i = maior
