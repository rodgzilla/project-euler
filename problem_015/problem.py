def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    print binomial(40, 20)
