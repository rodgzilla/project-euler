s = ''
i = 0
while len(s) < 1000001:
    s += str(i)
    i += 1
l = [s[1], s[10], s[100], s[1000], s[10000], s[100000], s[1000000]]
res = 1
for val in map(int, l):
    res *= val
print(res)
