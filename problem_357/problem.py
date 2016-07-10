import pickle

with open('../tools/prime_number_set', 'rb') as f:
    primes = pickle.load(f)
    print('loading done')

valid_numbers = set(range(1, 100000001))
i = 1
j = 1
prod = 1
while prod <= 100000000 or j != 1:
    if prod > 100000000 or i < j:
        i += 1
        j = 1
        prod = i * j
        continue
    print(i)
    if i + j not in primes:
        valid_numbers.remove(prod)
    j += 1
    prod = i * j
print(sum(valid_numbers))


# for i in range(1, 10001):
#     print(i)
#     if i % 2 == 0:
#         inc = 1
#         j = 1
#     else:
#         inc = 2
#         j = 2
#     prod = i * j
#     while prod < 100000000:
#         if i + j not in primes:
#             non_valid.add(prod)
#         j += inc
#         prod = i * j
# print((100000000 * 100000001) // 2 - (49999999 + 1) ** 2 - sum(non_valid))
