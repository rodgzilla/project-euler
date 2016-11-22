def convert_strings_to_grid(strings):
    return [list(map(int, s)) for s in strings]

def load_grids():
    f = open('p096_sudoku.txt')

    buf = []
    grids = []
    line_counter = 0

    for line in f.readlines():
        if line_counter % 10 == 0:
            if line_counter != 0:
                grids.append(convert_strings_to_grid(buf))
                buf = []
        else:
            buf.append(line[:-1] if line[-1] == '\n' else line)
        line_counter += 1
    grids.append(convert_strings_to_grid(buf))
    f.close()

    return grids

def solve(grid):
    pass

def compute_solution(solved_grids):
    return sum([100 * grid[0][0] + 10 * grid[0][1] + grid[0][2] for grid in solved_grids])

def print_grids(grids):
    for grid in grids:
        print('\n\n########################################')
        for line in grid:
            print(*line)
        print('########################################')

if __name__ == '__main__':
    grids = load_grids()
    print_grids(grids)
