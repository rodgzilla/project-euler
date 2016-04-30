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

def find_sequence(n):
    primes = eratosthene(n)
    for prime in primes:
        for i in range(1, n):
            if prime + i in primes and prime + 2 * i in primes:
                prime_1, prime_2, prime_3 = list(str(prime)), list(str(prime + i)), list(str(prime + 2 * i))
                prime_1.sort()
                prime_2.sort()
                prime_3.sort()
                if prime_1 == prime_2 == prime_3 :
                    print "prime =", prime, "i =", i, "===>", prime, prime + i, prime + 2 * i

if __name__ == '__main__':
    find_sequence(10000)
