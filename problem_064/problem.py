import math
import fractions

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

squares = {i * i for i in range(101)}
print(sum([1 if len(continued_fraction(n)) % 2 == 0 else 0 for n in range(2, 10001) if n not in squares]))
