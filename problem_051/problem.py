from itertools import product

def eratosthene(n):
    l = range(2, n / 2 + 1)
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def prime_replacement(primes, prime):
    result = []
    prime_str = list(str(prime))

    for take_vector in product([False, True], repeat = len(prime_str)):
        if take_vector == (False,) * len(prime_str) or \
           take_vector == (True,) * len(prime_str):
            continue
        new_number_shape = ''.join([prime_str[i] if take_vector[i] else '*' for i in range(len(prime_str))])
        temporary = []
        for n in [str(i) for i in range(10)]:
            number_subs = int(new_number_shape.replace('*', n))
            if len(str(number_subs)) < len(new_number_shape):
                continue
            if number_subs in primes:
                temporary.append(number_subs)
        if len(temporary) == 8:
            return temporary

def answer():
    primes = eratosthene(1000000)
    primes_list = list(primes)
    primes_list.sort()
    for prime_number in primes_list:
        res = prime_replacement(primes, prime_number)
        if res is not None:
            return res
    return []

if __name__ == '__main__':
    ans = sorted(answer())
    print(ans)
    print(ans[0])
