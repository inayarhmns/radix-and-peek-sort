from memory_profiler import profile
def counting_sort(A, exp, base):
    n = len(A)
    B = [0] * n
    count = [0] * base

    for i in range(n):
        index = (A[i] // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (A[i] // exp) % base
        B[count[index] - 1] = A[i]
        count[index] -= 1
        i -= 1

    return B

def radix_sort(A):
    max_num = max(A)
    exp = 1

    while max_num // exp > 0:
        A = counting_sort(A, exp, 10)
        exp *= 10
    return A





