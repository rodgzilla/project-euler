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

def are_compatible(p1, p2):
    sp1, sp2 = str(p1), str(p2)
    return is_prime(int(sp1 + sp2)) and is_prime(int(sp2 + sp1))

def find_valid_sets(primes, set_size):
    if set_size == 2:
        print('size 2 beginning')
        yield from ((p1, p2) for p1 in primes for p2 in primes if p1 < p2 and are_compatible(p1, p2))
        print('size 2 finished')
    else:
        print('size %d beginning' % set_size)
        res = set()
        for valid_set_lower_size in find_valid_sets(primes, set_size - 1):
            for prime in primes:
                if prime not in valid_set_lower_size and all((are_compatible(prime, x) for x in valid_set_lower_size)):
                    res.add(tuple(sorted(valid_set_lower_size + (prime,))))
        yield from list(res)
        print('size %d finished' % set_size)
    

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
primes = sorted(eratosthene(9000))
valid_sets = list(find_valid_sets(primes, 5))
print(valid_sets)
print(len(valid_sets))
res = min(valid_sets, key=sum)
print(res)
print(sum(res))


