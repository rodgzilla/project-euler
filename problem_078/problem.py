def pentagonal_number(n):
    return (3 * n**2 - n) // 2

def partition_number(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    res = 0
    i = 2
    k = 1
    while n >= pentagonal_number(k):
        res += (1 if k % 2 else - 1 ) * partition_number(n - pentagonal_number(k), memo)
        i += 1
        k = i // 2
        if i % 2:
            k = -k
    memo[n] = res
    return res

memo = {}
i = 0
while partition_number(i, memo) % 1000000 != 0:
    i += 1
print(i, partition_number(i, memo))
