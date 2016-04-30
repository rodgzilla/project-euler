import sys

def enumerate_triplet(max_value):
    for a in xrange(1, max_value + 1):
        for b in xrange(a, max_value - a):
            yield (a, b, max_value - a - b)

def find_pythagorean_triplet(max_value):
    for a, b, c in enumerate_triplet(max_value):
        if a * a + b * b == c * c:
            return (a, b, c)


if __name__ == '__main__':
    a, b, c = find_pythagorean_triplet(int(sys.argv[1]))
    print a * b * c

    
