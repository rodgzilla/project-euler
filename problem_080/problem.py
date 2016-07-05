def integer_part_sqrt(n):
    mini, maxi = 0, n // 2
    middle = (mini + maxi) // 2
    while not middle ** 2 <= n < (middle + 1) ** 2:
        if middle ** 2 < n:
            mini = middle
        else:
            maxi = middle
        middle = (mini + maxi) // 2
    return middle

s = set(range(1, 101)) - set([i**2 for i in range(1, 11)])
res = 0
for n in s:
    expansion = integer_part_sqrt(n*10**200)
    res += sum(map(int, str(expansion)[:-1]))
print(res)
