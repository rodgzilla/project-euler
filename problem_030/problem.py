def is_valid(n):
    digit_sum = 0
    new_n = n
    while not new_n == 0:
        digit_sum += (new_n % 10) ** 5
        new_n //= 10
    return digit_sum == n

res = 0
for i in range(2, 1000000):
    if is_valid(i):
        res += i
        
print(res)
