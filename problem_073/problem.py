from fractions import Fraction, gcd

def compute_solution(inf, sup, max_n):
    res = 0
    for denum in range(2, max_n + 1):
        num = denum // 3
        current = Fraction(num, denum)
        while not inf <= current <= sup:
            num += 1
            current = Fraction(num, denum)

        while inf <= current <= sup:
            if gcd(num, denum) == 1:
                res += 1
            num += 1
            current = Fraction(num, denum)


    return res - 2

print(compute_solution(Fraction(1, 3), Fraction(1, 2), 12000))
