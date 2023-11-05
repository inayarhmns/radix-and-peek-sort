from memory_profiler import profile
def merge(A, p, q, r):
    L = [i for i in A[p:q+1]]
    R = [i for i in A[q+1:r+1]]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0
    j = 0
    for k in range (p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def peeksort(A,l,r,e,s):
    if e == r or s == l:
        return
    m = (r+l)//2
    if m <= e:
        peeksort(A, e+1, r, e+1, s)
        merge(A, l, e, r)
    elif m >= s:
        peeksort(A, l, s-1, e, s-1)
        merge(A, l, s-1, r)
    else:
        i = extend_run_left(A, m, l)
        j = extend_run_right(A, m, r)
        if i == l and j == r and l == 0 and r == len(A)-1: return A
        if i == l and j == r: return
        if m - i < j - m:
            peeksort(A, l, i-1, e, i-1)
            peeksort(A, i, r, j, s)
            merge(A, l, i-1, r)
        else:
            peeksort(A, l, j, e, i)
            peeksort(A, j+1, r, j+1, s)
            merge(A, l, j, r)
    return A



def extend_run_left(A, m, left):
    i = m
    while i > left and A[i - 1] <= A[i]:
        i -= 1
    return i 
    
def extend_run_right(A, m, right):
    j = m
    while j < right and A[j] <= A[j + 1]:
        j += 1
    return j


def peek_sort(A):
    return peeksort(A, 0, len(A)-1, 0, len(A)-1)



import random

def dataset_sorted(n):
    return [i+1 for i in range (n)]

def dataset_reversed(sorted):
    return list(reversed(sorted))

def dataset_random(n):
    return random.choices(range(n),k=n)




sorted_k = dataset_sorted(1000)
random_k = dataset_random(1000)
reversed_k = dataset_reversed(sorted_k)

sorted_s = dataset_sorted(10000)
random_s = dataset_random(10000)
reversed_s = dataset_reversed(sorted_s)

sorted_b = dataset_sorted(100000)
random_b = dataset_random(100000)
reversed_b = dataset_reversed(sorted_b)


# def macaller():
#     makearray()
# def makearray():
#     makeanother()
# def makeanother():
#     L = [i for i in range(1000)]

# A = [4, 5, 6, 2]
# print(peek_sort(A))
# import os 
# import psutil
# def test_peek_sort():
#     print(peek_sort(reversed_b))
# @profile
# def peeek():
#     print(peek_sort(sorted_k))
# peeek()
# # test_peek_sort()
# A = sorted_b
# p = 0
# q = len(A)//2
# r = len(A)-1
# process1 = psutil.Process(os.getpid()).memory_info().rss
# # L = [i for i in A[p:q+1]]
# # R = [i for i in A[q+1:r+1]]
# # peek_sort(sorted_b)
# merge(A, p, q, r)
# # macaller()
# process2 = psutil.Process(os.getpid()).memory_info().rss
# print(process2-process1)