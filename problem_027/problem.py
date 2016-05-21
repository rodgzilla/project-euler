from functools import partial

def prime_number_set(max_prime_value):
    prime_set = set([2])
    current_number = 2
    last_prime = 2

    while current_number < max_prime_value:
        for prime in prime_set:
            if current_number % prime == 0:
                break
        else:
            prime_set.add(current_number)
            last_prime = current_number
        current_number += 1

    return prime_set

def sequence_element(n, a, b):
    return n * n + a * n + b

def prime_seq_len(primes, seq):
    n = 0
    while seq(n) in primes: n += 1
    return n

def find_solution():
    prime_numbers = prime_number_set(100000)
    print('Init done')
    max_a = max_b = 0
    max_seq_len = -1
    for b in prime_number_set(1000):
        for a in range(-1000, 1001):
            if a + b + 1 not in prime_numbers:
                continue
            seq_len = prime_seq_len(prime_numbers, partial(sequence_element, a=a, b=b))
            if seq_len > max_seq_len:
                max_a = a
                max_b = b
                max_seq_len = seq_len
    return max_a, max_b
a, b = find_solution()
print(a,b,a*b)

