from itertools import product
import sys

sys.setrecursionlimit(2500)

def eratosthene(n):
    l = range(2, n // 2 + 1)
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def find_closest_prime(primes_list, n):
    pass

def are_compatible(p1, p2):
    sp1, sp2 = str(p1), str(p2)
    return is_prime(int(sp1 + sp2)) and is_prime(int(sp2 + sp1))

def find_primes_combination(primes, index, n, l=[]):
    if n == 0:
        if len(l) == 5:
            return l
        return []
    if index < 0:
        return []
    res = []
    if primes[index] <= n and all((are_compatible(primes[index], prev_prim) for prev_prim in l)):
        res = find_primes_combination(primes, index - 1, n - primes[index], l + [primes[index]])
    return res + find_primes_combination(primes, index - 1, n, l)
    

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
primes = sorted(eratosthene(10000))
i = 792
while True:
    print(i)
    res = find_primes_combination(primes, len(primes) - 1, i)
    if not res == []:
        print(*res, sep=' ')
        break
    i += 1
print(i)

# def answer():
#     primes = eratosthene(10000)
#     primes.remove(2)
#     primes.remove(5)
#     pl = sorted(list(primes))
#     res = []
#     print(len(primes))
    
#     for i in range(len(pl)):
#         for j in range(i + 1, len(pl)):
#             if not are_compatible(pl[i], pl[j]):
#                 continue
#             for k in range(j + 1, len(pl)):
#                 if not all([are_compatible(pl[k], pl[n]) for n in [i, j]]):
#                     continue
#                 for l in range(k + 1, len(pl)):
#                     if not all([are_compatible(pl[k], pl[n]) for n in [i, j, k]]):
#                         continue
#                     for m in range(l + 1, len(pl)):
#                         if not all([are_compatible(pl[k], pl[n]) for n in [i, j, k, l]]):
#                             continue
#                         print(pl[i], pl[j], pl[k], pl[l], pl[m])
#                         res.append(pl[i] + pl[j] + pl[k] + pl[l] + pl[m])
#     return sorted(res)

# print(answer()[0])
# print(are_compatible(673, 3))
