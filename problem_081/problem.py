with open('p081_matrix.txt') as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(map(int, line[:-1].split(','))))
path_matrix = []
for i, line in enumerate(matrix):
    current_path_matrix_line = []
    for j, value in enumerate(line):
        if i == 0:
            if j == 0:
                current_path_matrix_line.append(value)
            else:
                current_path_matrix_line.append(current_path_matrix_line[-1] + value)
        else:
            if j == 0:
                current_path_matrix_line.append(path_matrix[i - 1][0] + value)
            else:
                current_path_matrix_line.append(min(path_matrix[i - 1][j], current_path_matrix_line[j - 1]) + value)
    path_matrix.append(current_path_matrix_line)

print(path_matrix[-1][-1])
