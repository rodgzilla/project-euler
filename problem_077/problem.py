from math import sqrt
from collections import defaultdict

def eratosthene(n):
    l = range(2, int(sqrt(n)) + 1)
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def compute_decomposition(n, primes, decomp_dict):
    if n in decomp_dict:
        return decomp_dict[n]
    if n in primes:
        decomp_dict[n].add((n,))
    for i in range(2, n // 2 + 1):
        if i not in primes:
            continue
        for sub_dec in compute_decomposition(n - i, primes, decomp_dict):
            dec = (i,) + sub_dec
            if sum(dec) == n:
                decomp_dict[n].add(tuple(sorted(dec)))
    return decomp_dict[n]


def compute_solution(max_value):
    primes = eratosthene(max_value)
    decomp_dict = defaultdict(set)
    for i in range(2, max_value):
        compute_decomposition(i, primes, decomp_dict)
        if len(decomp_dict[i]) > 5000:
            return i
    return decomp_dict
    
print(compute_solution(100))
