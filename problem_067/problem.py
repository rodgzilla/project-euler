triangle = [list(map(int, line.split())) for line in open('triangle.txt').readlines()]
max_sums = []

for i, line in enumerate(triangle):
    if i == 0:
        max_sums.append([line[0]])
    else:
        max_sums.append([])
        for j, value in enumerate(line):
            if j == 0:
                max_sums[-1].append(max_sums[-2][0] + value)
            elif j == len(line) - 1:
                max_sums[-1].append(max_sums[-2][-1] + value)
            else:
                max_sums[-1].append(max([max_sums[-2][j - 1], max_sums[-2][j]]) + value)

print(max(max_sums[-1]))
    
