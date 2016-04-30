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

def test_number(n, primes):
    prime_index = 0
    while primes[prime_index] < n:
        square = 1
        while primes[prime_index] + 2 * square ** 2 < n:
            square += 1
        if primes[prime_index] + 2 * square ** 2 == n:
            return False
        prime_index += 1
    return True

def find_number(max_value):
    primes = eratosthene(max_value)
    primes_list = list(primes)
    primes_list.sort()
    n = 2
    while True:
        if n % 2 == 1 and n not in primes and test_number(n, primes_list):
            return n
        n += 1

if __name__ == '__main__':
    max_value = 1000000
    print find_number(max_value)
