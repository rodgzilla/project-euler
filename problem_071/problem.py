from fractions import Fraction

def find_solution(max_d):
    res = []
    for d in range(1, max_d + 1):
        res.append(Fraction(3 * d // 7, d))
    res.sort()
    target = Fraction(3,7)
    for value in res[::-1]:
        if value != target:
            return value

print(find_solution(1000000).numerator)
