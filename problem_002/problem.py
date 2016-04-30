if __name__ == '__main__':
    result = 0
    a = b = 1
    while a <= 4000000:
        b = a + b 
        a = b - a
        if a % 2 == 0:
            result += a
    print result
