import math
from fractions import Fraction as frac

def generate_development(seq):
    seq_period = seq[1:]
    yield seq[0]
    i = 0
    while True:
        yield seq_period[i]
        i = (i + 1) % len(seq_period)

def continued_fraction(n):
    initial_term = math.floor(math.sqrt(n))
    terms = [initial_term]

    seen = set()
    num = 1
    int_denum = - initial_term
    while (num, int_denum) not in seen:
        seen.add((num, int_denum))
        new_denum = (n - int_denum ** 2) // num
        int_num = - int_denum
        new_term = math.floor((math.sqrt(n) + int_num) / new_denum)
        terms.append(new_term)
        num = new_denum
        int_denum = int_num - new_denum * new_term
    return terms

def compute_sum(sequence):
    current = 0
    for i in range(len(sequence) - 1, 0, -1):
        current = frac(1, sequence[i] + current)
    current += sequence[0]
    return current

def solve_eq(d):
    x, y = 0, 0
    seq_size = 2
    reduced_sequence = continued_fraction(d)
    while x**2 - d * y ** 2 != 1:
        generalized_sequence = generate_development(reduced_sequence)
        sequence = [generalized_sequence.send(None) for _ in range(seq_size)]
        current = 0
        for i in range(len(sequence) - 1, 0, -1):
            current = frac(1, sequence[i] + current)
        current += sequence[0]
        x = current.numerator
        y = current.denominator
        seq_size += 1
    return x, y


squares = {i * i for i in range(1, 33)}
max_d = -1
max_x_value = -1
for d in (x for x in range(2, 1001) if x not in squares):
    x, _ = solve_eq(d)
    if x > max_x_value:
        max_d = d
        max_x_value = x
print(max_d)
