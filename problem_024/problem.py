def permutations(n):
    if n == 1:
        return [[0]]
    return [p[:i] + [n - 1] + p[i:] for p in permutations(n - 1) for i in range(n)]

if __name__ == '__main__':
    perms_str = [''.join([str(x) for x in p]) for p in permutations(10)]
    perms_str.sort()
    print perms_str[999999]

