def results():
    numbers = []
    for i in range(1, 100000):
        j = 1
        s = set()
        res = ''
        while len(s) < 9 and '0' not in s: # while the number is not pandigital
            prev_size = len(s)
            n = str(i * j) # compute the next product
            s.update(n)
            if not prev_size + len(n) == len(s): # if we find a digit already encountered, we stop.
                break
            res += n
            if int(res) > 999999999:
                break
            j += 1
        if not res == '' and int(res) < 1000000000 and len(s) == 9 and '0' not in s:
            numbers.append(int(res))
    return numbers
    
print(max(results()))
