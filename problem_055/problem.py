def is_lychrel(n):
    s_n = str(n)
    s_n = str(n + int(''.join(s_n[::-1])))
    for _ in range(50):
        if all((s_n[i] == s_n[-i - 1] for i in range(len(s_n) // 2))):
            return False
        s_n = str(int(s_n) + int(''.join(s_n[::-1])))
    return True
        
print(sum([1 if is_lychrel(n) else 0 for n in range(1, 10000)]))
