s_2 = set('012')

possible_multiple_last_digit = \
                               {0: [1,2,3,4,5,6,7,8,9], \
                                1 : [1, 2], \
                                2 : [1, 5, 6], \
                                3 : [4, 7], \
                                4 : [3, 5, 8], \
                                5 : [2, 4, 6, 8], \
                                6 : [2, 5, 7], \
                                7 : [3, 6], \
                                8 : [4, 5, 9], \
                                9 : [8, 9] \
                            }
                                
def k(n):
    k = 1
    current = n
    current_set = set(str(current))
    while not current_set.issubset(s_2):
        k += 1
        current = k * n
        current_set = set(str(current))
    return k

def k_astucious(n):
    last_digit = n % 10

    k = 0
    current = n
    current_set = set(str(current))
    while True:
        for ld in possible_multiple_last_digit[last_digit]:
            multiplier = 10 * k + ld
            current = n * multiplier
            current_set = set(str(current))
            if current_set.issubset(s_2):
                return multiplier
        k += 1

if __name__ == '__main__':
    res = 0
    print(k_astucious(3214))
    for i in range(1, 101):
        res += k_astucious(i)
    print(int(res))
