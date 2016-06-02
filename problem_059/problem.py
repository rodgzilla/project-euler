from collections import Counter
from itertools import product

# code for finding the correct key

cipher = list(map(int, open('cipher.txt', 'r').read().split(',')))
ciphers = [cipher[i::3] for i in range(3)]
# print(*ciphers, sep='\n\n')
most_commons_top = [Counter(c).most_common()[:3] for c in ciphers]
for most_commons in product(*most_commons_top):
    print('####################')
    print([most_frequent for most_frequent, _ in most_commons])
    key = [most_frequent ^ ord('e') for most_frequent, _ in most_commons]
    if not all((ord('a') <= k <= ord('z') for k in key)):
        continue
    print(key)
    decipher = ''.join([chr(c ^ key[i % 3]) for i, c in enumerate(cipher)])
    print(decipher)

key = 'god'
result = sum([c ^ ord(key[i % 3]) for i, c in enumerate(cipher)])
print(result)
