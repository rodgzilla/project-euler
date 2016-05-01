t = [0] * 28124
for i in range(1, 28124):
    for j in range(2 * i, 28124, i):
        t[j] += i
abundant_number = [i for i, value in enumerate(t) if value > i]

writable_as_a_sum = set()
for i in range(len(abundant_number)):
    for j in range(i, len(abundant_number)):
        if abundant_number[i] + abundant_number[j] < 28124:
            writable_as_a_sum.add(abundant_number[i] + abundant_number[j])
        else:
            break

res = 0
for i in range(28124):
    if i not in writable_as_a_sum:
        res += i
print(res)
