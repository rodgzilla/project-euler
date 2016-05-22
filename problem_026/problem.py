def exp_len(n):
    dividend = 1
    dividends = set()
    expansion = []
    while dividend not in dividends:
        dividends.add(dividend)
        expansion.append(dividend // n)
        dividend = dividend % n * 10
    return expansion

def find_solution():
    max_l = -1
    v = None
    for i in range(1, 1001):
        l = len(exp_len(i))
        if l > max_l:
            v = i
            max_l = l
    return v

print(find_solution())
        
