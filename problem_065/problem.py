from fractions import Fraction as frac

def compute_sum(sequence):
    current = 0
    for i in range(len(sequence) - 1, 0, -1):
        current = frac(1, sequence[i] + current)
    current += sequence[0]
    return current
        
seq = [2, 1, 2] + [(i // 3 + 2) * 2 if i % 3 == 2 else 1 for i in range(96)] + [1]
print(sum(map(int, str(compute_sum(seq).numerator))))
