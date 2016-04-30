def factor(n):
    current = n
    result = []
    divisor = 2
    while current != 1:
        if current % divisor == 0:
            result.append(divisor)
            current /= divisor
            divisor = 2
        else:
            divisor += 1
    return result

def find_consecutive(prime_factor_number):
    current = 2
    count = 0

    while count != prime_factor_number:
        if current % 1000 == 0:
            print current
        if len(set(factor(current))) >= prime_factor_number:
            count += 1
        else:
            count = 0
        current += 1
    print current
    return [current - i for i in range(prime_factor_number, 0, -1)]

if __name__ == '__main__':
    print find_consecutive(4)
