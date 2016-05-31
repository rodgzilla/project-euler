from itertools import permutations

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

def is_pandigital(n):
    str_n = str(n)
    set_n = set(str_n)
    pandigital_number = set(''.join([str(x) for x in range(1, len(str_n) + 1)]))
    return set_n == pandigital_number

def find_answer():
    pantadigital_primes = []
    for perm_size in range(9, 0, -1):
        for perm in sorted(list(permutations(range(1, perm_size + 1))), reverse = True):
            n = int(''.join(map(str,perm)))
            if is_prime(n):
                pantadigital_primes.append(n)
    return pantadigital_primes

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
# print(is_prime(656498119189819849879876546413257357354348676654316573))
answers = find_answer()
print(max(answers))

