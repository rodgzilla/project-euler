import math

with open('p099_base_exp.txt') as f:
    l = [(tuple(map(int,line[:-1].split(','))), i + 1) for i, line in enumerate(f.readlines())]

l = [(c[1] * math.log(c[0]), i) for c, i in l]
print(max(l)[1], sep='\n')
