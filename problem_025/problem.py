def fibo(nb_digit):
    a = 1
    b = 1
    i = 2
    while len(str(b)) < nb_digit:
        a, b, i = b, a + b, i + 1
    return i

if __name__ == '__main__':
    print fibo(1000)
