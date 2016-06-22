from fractions import Fraction

def prime_number_decomposition(n):
    dec = []
    div = 2
    while n != 1:
        if n % div == 0:
            dec.append(div)
            n //= div
        else:
            div += 1
    return dec

def totient(n):
    res = n
    for prime in set(prime_number_decomposition(n)):
        res *= 1 - Fraction(1, prime)
    return int(res)

def compute_solution():
    return max([(n, Fraction(n, totient(n))) for n in range(2, 1000001)], key=lambda x:x[1])


print(compute_solution())
