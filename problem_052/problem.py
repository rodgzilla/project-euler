def test_number(n):
    s1 = set(str(n))
    s2 = set(str(2 * n))
    s3 = set(str(3 * n))
    s4 = set(str(4 * n))
    s5 = set(str(5 * n))
    s6 = set(str(6 * n))
    
    if s1 == s2 == s3 == s4 == s5 == s6:
        return True
    return False

def find_number():
    n = 1

    while not test_number(n):
        n += 1

    return n

if __name__ == '__main__':
    print find_number()
