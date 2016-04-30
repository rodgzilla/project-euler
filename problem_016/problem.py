def rapid_exp(n, k):
    if k == 0:
        return 1

    if k == 1:
        return n

    x = rapid_exp(n, int(k / 2))

    if k % 2 == 0:
        return x * x
    return x * x * n

if __name__ == '__main__':
    result = rapid_exp(2, 1000)
    print sum([int(x) for x in str(result)])
