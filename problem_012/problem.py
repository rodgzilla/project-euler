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

def number_of_divisors_totient(n):
    decomposition = prime_decomposition(n)
    histogram = {}

    for factor in decomposition:
        histogram[factor] = histogram.get(factor, 0) + 1

    result = 1

    for x in histogram.values():
        result *= (x + 1)

    return result


def find_largest_decomposition():
    i = 1
    while True:
        triangle_number = (i * (i + 1)) / 2
        divisors_number = number_of_divisors_totient(triangle_number)
        if divisors_number >= 500:
            print triangle_number, divisors_number
            return triangle_number
        i += 1

if __name__ == '__main__':
    print find_largest_decomposition()
