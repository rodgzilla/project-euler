def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def sum_digits_factorial(n):
    fact = factorial(n)
    return sum([int(x) for x in str(fact)])

if __name__ == '__main__':
    print sum_digits_factorial(100)
