import sys
import math

def sieve(size):
    int_list = range(1, size + 1)
    print int_list
    for i in range(int(math.sqrt(size))):
        multiple = 1
        while int_list[i] * multiple < size

if __name__ == '__main__':
    sieve(int(sys.argv[1]))

