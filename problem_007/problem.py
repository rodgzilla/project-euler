import sys

def prime_number_list(size):
    prime_list = []
    current_number = 2

    while len(prime_list) < size:
        for prime in prime_list:
            if current_number % prime == 0:
                break
        else:
            prime_list.append(current_number)
        current_number += 1
    return prime_list

if __name__ == '__main__':
    print prime_number_list(int(sys.argv[1]))[-1]
