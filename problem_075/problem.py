from collections import defaultdict

def generate_triple(m, n):
    a = (m ** 2 - n ** 2)
    b = (2 * m * n)
    c = (m ** 2 + n ** 2)
    return tuple(sorted([a, b, c]))

def generate_multiple(a, b, c, max_value):
    res = []
    current_a = a
    current_b = b
    current_c = c
    while current_a + current_b + current_c <= max_value:
        yield (current_a, current_b, current_c)
        current_a += a
        current_b += b
        current_c += c

def compute_solution(max_value):
    a, b, c = 3, 4, 5
    m, n = 2, 1
    results = defaultdict(set)
    while a + b + c <= max_value or n != 1:
        if a + b + c > max_value:
            m += 1
            n = 1
            a, b, c = generate_triple(m, n)
            continue
        for new_a, new_b, new_c in generate_multiple(a, b, c, max_value):
            results[new_a + new_b + new_c].add((new_a, new_b, new_c))
        if n == m - 1:
            m += 1
            n = 1
        else:
            n += 1
        a, b, c = generate_triple(m, n)
    return sum([len(results[perimeter]) == 1 for perimeter in results])
            
print(compute_solution(1500000))
