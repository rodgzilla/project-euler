from math import factorial

def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

res = 0
for n in range(1, 101):
    for k in range(1, n):
        res += 1 if binom(n, k) > 1000000 else 0

print(res)
