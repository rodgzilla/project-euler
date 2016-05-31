from itertools import permutations

pandigits_tuples = [(i,) + perm for i in range(1, 10) for perm in permutations([x for x in range(0, 10) if x != i])]
pandigits_numbers = (''.join([str(x) for x in t]) for t in pandigits_tuples)

primes = [2, 3, 5, 7, 11, 13, 17]
valid_numbers = []
for n in pandigits_numbers:
    for i in range(7):
        if not int(n[i + 1: i + 4]) % primes[i] == 0:
            break
    else:
        valid_numbers.append(int(n))

print(sum(valid_numbers))
