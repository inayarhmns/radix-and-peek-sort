import random
from peeksort import peek_sort 
from radixsort import radix_sort
import tracemalloc
import time
def dataset_sorted(n):
    return [i+1 for i in range (n)]

def dataset_reversed(sorted):
    return list(reversed(sorted))

def dataset_random(n):
    return random.choices(range(n),k=n)

def elapsed_since(start):
    elapsed_time = (time.time() - start) * 1000  # Convert to milliseconds
    return elapsed_time

def get_time():
    return time.time()

sorted_k = dataset_sorted(1000)
random_k = dataset_random(1000)
reversed_k = dataset_reversed(sorted_k)

sorted_s = dataset_sorted(10000)
random_s = dataset_random(10000)
reversed_s = dataset_reversed(sorted_s)

sorted_b = dataset_sorted(100000)
random_b = dataset_random(100000)
reversed_b = dataset_reversed(sorted_b)
with open('sorted_k.txt', 'w', encoding='utf-8') as file:
    file.write(str(sorted_k))
with open('random_k.txt', 'w', encoding='utf-8') as file:
    file.write(str(random_k))
with open('reversed_k.txt', 'w', encoding='utf-8') as file:
    file.write(str(reversed_k))
with open('sorted_s.txt', 'w', encoding='utf-8') as file:
    file.write(str(sorted_s))
with open('random_s.txt', 'w', encoding='utf-8') as file:
    file.write(str(random_s))
with open('reversed_s.txt', 'w', encoding='utf-8') as file:
    file.write(str(reversed_s))
with open('sorted_b.txt', 'w', encoding='utf-8') as file:
    file.write(str(sorted_b))
with open('random_b.txt', 'w', encoding='utf-8') as file:
    file.write(str(random_b))
with open('reversed_b.txt', 'w', encoding='utf-8') as file:
    file.write(str(reversed_b))

datasets = {
    'sorted_k':sorted_k,
    'random_k':random_k,
    'reversed_k':reversed_k,
    'sorted_s':sorted_s,
    'random_s':random_s,
    'reversed_s':reversed_s,
    'sorted_b':sorted_b,
    'random_b':random_b,
    'reversed_b':reversed_b,
}
# average of n testing for time execution in ms
def average_timetest(algo, dataset):
    n = 3
    time_sums = 0
    if(algo == 'radix'):
        for i in range(n):
            start = get_time()
            print(radix_sort(dataset))
            time = elapsed_since(start)
            print(time)
            time_sums += time
    else:
        for i in range(n):
            start = get_time()
            print(peek_sort(dataset))
            time = elapsed_since(start)
            print(time)
            time_sums += time
    return time_sums/n

# average of n testing for memory PEAK in bytes
def average_memtest(algo, dataset):
    n = 3
    mem_sum = 0
    if(algo == 'radix'):
        for i in range(n):
            tracemalloc.start()
            print(radix_sort(dataset))
            memory_peak = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            print(memory_peak)
            mem_sum += memory_peak
    else:
        for i in range(n):
            tracemalloc.start()
            print(peek_sort(dataset))
            memory_peak = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            print(memory_peak)
            mem_sum += memory_peak
    return f"{mem_sum/n} B\n"

# with open('memory.txt', 'w', encoding='utf-8') as file:
#     for i in datasets:
#         mem = average_memtest('radix', datasets.get(i))
#         file.write(mem)
#     for i in datasets:
#         mem = average_memtest('peek', datasets.get(i))
#         file.write(mem)

# with open('time.txt', 'w', encoding='utf-8') as file:
#     for i in datasets:
#         t = average_timetest('radix', datasets.get(i))
#         file.write("{:.2f} ms\n".format(t))
#     for i in datasets:
#         t = average_timetest('peek', datasets.get(i))
#         file.write("{:.2f} ms\n".format(t))

 