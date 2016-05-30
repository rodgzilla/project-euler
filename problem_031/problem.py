coins = [1, 2, 5, 10, 20, 50, 100, 200]

def find_solutions(value, coin_index=0):
    if coin_index >= len(coins):
        return []
    res = []
    i = 0
    while i * coins[coin_index] < value:
        for solution in find_solutions(value - i * coins[coin_index], coin_index + 1):
            res.append((i,) + solution)
        i += 1

    if i * coins[coin_index] == value:
        res.append((i,))

    return res

print(len(find_solutions(200)))
