from math import sqrt
from collections import defaultdict, Counter
from fractions import Fraction

def reverse_erathos(n):
    d = defaultdict(set)
    for i in range(2, n + 1):
        if i not in d:
            j = 2 * i
            while j <= n:
                d[j].add(i)
                j += i
    return d

def totient(n, prime_decs):
    if n not in prime_decs:
        return n - 1
    res = n
    for prime in prime_decs[n]:
        res *= 1 - Fraction(1, prime)
    return int(res)

def compute_solution(n):
    c = 1
    prime_decs = reverse_erathos(n)
    res = 0
    for i in range(2, n + 1):
        if c % 50000 == 0:
            print(c)
        res += totient(i, prime_decs)
        c += 1
    return res

print(compute_solution(1000000), sep='\n')
