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

def is_truncable(primes, n):
    str_n = str(n)
    for i in range(1, len(str_n) + 1):
        if int(str_n[:i]) not in primes:
            return False
    for i in range(len(str_n)):
        if int(str_n[i:]) not in primes:
            return False

    return True

def find_truncatable_primes(n):
    primes = eratosthene(n)
    return [p for p in primes if is_truncable(primes, p) and p > 10]
    
if __name__ == '__main__':
    print sum(find_truncatable_primes(1000000))
