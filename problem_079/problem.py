from collections import defaultdict

with open('p079_keylog.txt') as f:
    lines = [line[:-1] for line in f.readlines()]
d = defaultdict(set)
for line in lines:
    d[line[0]].add(line[1])
    d[line[0]].add(line[2])
    d[line[1]].add(line[2])

items = sorted(list(d.items()), key=lambda x: -len(x[1]))
print(*([x[0] for x in items] + [0]), sep='')
