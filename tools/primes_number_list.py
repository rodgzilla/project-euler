import math
import pickle

def eratosthene(n):
    l = range(2, int(math.sqrt(n)) + 1)
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

with open('prime_number_list.txt', 'wb') as save_file:
    pickle.dump(eratosthene(100), save_file)

