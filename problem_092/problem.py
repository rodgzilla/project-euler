def chain(n, to_1, to_89):
    if n == 1 or n in to_1:
        return 1
    if n == 89 or n in to_89:
        return 89
    next_number = sum(map(lambda x: int(x)**2, str(n)))
    res = chain(next_number, to_1, to_89)
    (to_1 if res == 1 else to_89).add(n)
    return res

to_1 = set()
to_89 = set()
print(sum((chain(i, to_1, to_89) == 89 for i in range(1, 10000000))))
