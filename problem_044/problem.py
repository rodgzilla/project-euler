pentagonal_number = {n * (3 * n - 1) // 2 for n in range(1, 10000)}
min_d = 10000000
for n1 in pentagonal_number:
    for n2 in pentagonal_number:
        if n1 == n2:
            continue
        if n1 + n2 in pentagonal_number and \
           abs(n1 - n2) in pentagonal_number \
           and abs(n1 - n2) < min_d:
            print(n1, n2)
            min_d = abs(n1 - n2)
print(min_d)

