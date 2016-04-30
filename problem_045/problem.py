def compute_triangle_number(n):
    return int((n * (n + 1)) / 2)

def compute_pentagonal_number(n):
    return int((n * (3 * n - 1)) / 2)

def compute_hexagonal_number(n):
    return int(n * (2 * n - 1))

def find_solution():
    n_triangle = 1
    n_pentagonal = 1
    n_hexagonal = 1

    current_triangle_number = compute_triangle_number(1)
    current_pentagonal_number = compute_pentagonal_number(1)
    current_hexagonal_number = compute_hexagonal_number(1)

    res = []

    while len(res) < 3:
        if current_triangle_number == current_pentagonal_number == current_hexagonal_number:
            res.append(current_triangle_number)
            n_triangle += 1
            current_triangle_number = compute_triangle_number(n_triangle)
        elif current_triangle_number < current_pentagonal_number:
            n_triangle += 1
            current_triangle_number = compute_triangle_number(n_triangle)
        elif current_triangle_number > current_pentagonal_number:
            n_pentagonal += 1
            current_pentagonal_number = compute_pentagonal_number(n_pentagonal)
        else:
            if current_pentagonal_number < current_hexagonal_number:
                n_pentagonal += 1
                current_pentagonal_number = compute_pentagonal_number(n_pentagonal)
            else:
                n_hexagonal += 1
                current_hexagonal_number = compute_hexagonal_number(n_hexagonal)
    return res
            

if __name__ == '__main__':
    print(find_solution())
