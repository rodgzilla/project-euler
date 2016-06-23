from math import sqrt
from collections import defaultdict
from fractions import Fraction

def reverse_erathos(n):
    d = defaultdict(set)
    for i in range(2, int(sqrt(n)) + 2):
        if i not in d:
            j = i
            while j <= n:
                d[j].add(i)
                j += i
    return d

def totient(n, prime_decs):
    res = n
    for prime in prime_decs[n]:
        res *= 1 - Fraction(1, prime)
    return int(res)

def compute_solution():
    prime_decs = reverse_erathos(1000000)
    return max([(n, Fraction(n, totient(n, prime_decs))) for n in range(2, 1000001)], key=lambda x:x[1])

print(compute_solution())
