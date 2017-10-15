def eratosthene(n):
    l = range(2, n // 2 + 1)
    primes = set(range(2, n))

    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def find_solution(primes, sup = 50000000):
    valid_numbers = set()
    for x in primes:
        pow_2 = x ** 2

        if pow_2 > sup:
            break

        for y in primes:
            pow_3 = y ** 3
            sum_23 = pow_2 + pow_3

            if sum_23 > sup:
                break

            for z in primes:
                pow_4 = z ** 4
                sum_234 = sum_23 + pow_4
                if sum_234 < sup:
                    valid_numbers.add(sum_234)
    return len(valid_numbers)


if __name__ == '__main__':
    primes = sorted(eratosthene(7100))
    solution = find_solution(primes, sup = 50000000)
    print(solution)
