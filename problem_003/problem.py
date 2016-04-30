import sys

def prime_decomposition(n):
    decomposition = []
    i = 2
    while n > 1:
        if n % i == 0:
            decomposition.append(i)
            n = n / i
            i = 2
        else:
            i += 1

    return decomposition

if __name__ == '__main__':
    print prime_decomposition(int(sys.argv[1]))
