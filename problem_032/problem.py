import math

def mag(x):
    return int(math.log10(x)) + 1

def find_pandigitals_products():
    res = set()
    for i in range(2,100000):
        mag_i = mag(i)
        j = 2
        mag_j = mag(j)
        while mag_i + mag_j + mag(i * j) < 9: 
            j += 1
            mag_j = mag(j)
        while mag_i + mag_j + mag(i * j) == 9:
            s = set(str(i) + str(j) + str(i * j))
            if len(s) == 9 and '0' not in s:
                res.add(i * j)
            j += 1
            mag_j = mag(j)
    return res

print(sum(find_pandigitals_products()))
