import sys

def prime_number_list(max_prime_value):
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

    return list(prime_set)

if __name__ == '__main__':
#    print prime_number_list(int(sys.argv[1]))
    print sum(prime_number_list(int(sys.argv[1])))
