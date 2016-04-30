def find_couple():
    max_a, max_b = 0, 0
    max_sum = -1
    for a, b in ((a, b) for a in range(1, 100) for b in range(1, 100)):
        n = sum([int(x) for x in list(str(a ** b))])
        if n > max_sum:
            max_sum, max_a, max_b = n, a, b
    
    return max_sum, max_a, max_b

if __name__ == '__main__':
    print find_couple()
