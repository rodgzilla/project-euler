from itertools import permutations

def compute_5_gon(p):
    return [\
            [p[0], p[1], p[2]],
            [p[3], p[2], p[4]],
            [p[5], p[4], p[6]],
            [p[7], p[6], p[8]],
            [p[9], p[8], p[1]]
        ]

def is_valid(polygon):
    n = sum(polygon[0])
    return all((sum(line) == n for line in polygon[1:]))

def compute_valid_gons():
    res = []
    for perm in permutations(range(1, 11)):
        polygon = compute_5_gon(perm)
        if is_valid(polygon):
            res.append(polygon)
    return res

def rotate_notation(polygon):
    minimum = 11
    index_min = 10
    for i, line in enumerate(polygon):
        if line[0] < minimum:
            minimum = line[0]
            index_min = i
    return polygon[index_min:] + polygon[:index_min]
    

def compute_solution():
    valid_polygons = compute_valid_gons()
    valid_polygons_rotation = list(map(rotate_notation, valid_polygons))

    strings = [''.join([''.join(map(str, line)) for line in polygon]) for polygon in valid_polygons_rotation]
    return max([string for string in strings if len(string) == 16])


print(compute_solution())
    
