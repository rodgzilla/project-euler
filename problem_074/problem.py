from math import factorial

def digits(n):
    """
    From least to most significant.
    """
    while n:
        yield n % 10
        n //= 10

def pre_compute_digit_factorials():
    return {i : factorial(i) for i in range(10)}

def compute_cycle(n, fact):
    s = set()
    current = n
    while current not in s:
        s.add(current)
        current = sum(map(fact.get, digits(current)))
    return s

def compute_solution(max_n):
    fact = pre_compute_digit_factorials()
    res = 0
    for n in range(max_n + 1):
        if len(compute_cycle(n, fact)) == 60:
            res += 1

    return res

print(compute_solution(1000000))
