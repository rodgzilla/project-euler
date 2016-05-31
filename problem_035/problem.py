import math

def prime_number_set(max_value):
    """This function computes the set of prime numbers that are smaller
    than or equal to max_value.

    """
    int_list = range(2, max_value + 1)
    primes = set(int_list)

    for n in int_list:
        if n in primes:
            i = 2 * n
            while i <= max_value:
                if i in primes:
                    primes.remove(i)
                i += n
    return primes

def is_circular(primes, prime):
    nb_digits = int(math.log10(prime))
    for i in range(1, nb_digits + 1):
        right_part = prime % (10 ** i)
        left_part = prime // (10 ** i)
        rotated = right_part * (10 ** (nb_digits - i + 1)) + left_part
        if rotated not in primes:
            return False
    return True

def answer():
    primes = prime_number_set(1000000)
    return len([prime for prime in primes if is_circular(primes, prime)])

print(answer())
