max_p = -1
max_len = -1
for perimeter in range(3, 1001):
    l = []
    for first_side in range(1, perimeter):
        for second_side in range(1, perimeter - first_side):
            third_side = perimeter - first_side - second_side
            if first_side ** 2 + second_side ** 2 > third_side ** 2:
                break
            if first_side ** 2 + second_side ** 2 == third_side ** 2:
                l.append((first_side, second_side, third_side))
    if len(l) > max_len:
        max_len = len(l)
        max_p = perimeter
print(max_p)
