
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