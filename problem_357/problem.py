import pickle

with open('../tools/prime_number_set', 'rb') as f:
    primes = pickle.load(f)
    print('loading done')

valid_numbers = [True] * 100000001
i = 1
j = 1
prod = 1
while prod <= 100000000 or j != 1:
    if prod > 100000000 or i < j:
        i += 1
        j = 1
        prod = i * j
        continue
    if i + j not in primes:
        valid_numbers[prod] = False
    j += 1
    prod = i * j
print(sum([i for i, val in enumerate(valid_numbers) if val]))

