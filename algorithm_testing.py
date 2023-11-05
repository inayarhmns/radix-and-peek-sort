from peeksort import peek_sort 
from radixsort import radix_sort
import tracemalloc
import time
import json

def elapsed_since(start):
    elapsed_time = (time.time() - start) * 1000  # Convert to milliseconds
    return elapsed_time

def get_time():
    return time.time()


with open('sorted_k.txt', 'r') as file:
    # Read the contents of the file
    sorted_k = json.loads(file.read())
with open('random_k.txt', 'r') as file:
    # Read the contents of the file
    random_k = json.loads(file.read())
with open('reversed_k.txt', 'r') as file:
    # Read the contents of the file
    reversed_k = json.loads(file.read())
with open('sorted_s.txt', 'r') as file:
    # Read the contents of the file
    sorted_s = json.loads(file.read())
with open('random_s.txt', 'r') as file:
    # Read the contents of the file
    random_s = json.loads(file.read())
with open('reversed_s.txt', 'r') as file:
    # Read the contents of the file
    reversed_s = json.loads(file.read())
with open('sorted_b.txt', 'r') as file:
    # Read the contents of the file
    sorted_b = json.loads(file.read())
with open('random_b.txt', 'r') as file:
    # Read the contents of the file
    random_b = json.loads(file.read())
with open('reversed_b.txt', 'r') as file:
    # Read the contents of the file
    reversed_b = json.loads(file.read())


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

with open('memory.txt', 'w', encoding='utf-8') as file:
    for i in datasets:
        mem = average_memtest('radix', datasets.get(i))
        file.write(mem)
    for i in datasets:
        mem = average_memtest('peek', datasets.get(i))
        file.write(mem)

with open('time2.txt', 'w', encoding='utf-8') as file:
    for i in datasets:
        t = average_timetest('radix', datasets.get(i))
        file.write("{:.2f} ms\n".format(t))
    for i in datasets:
        t = average_timetest('peek', datasets.get(i))
        file.write("{:.2f} ms\n".format(t))
