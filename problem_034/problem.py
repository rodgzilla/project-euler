def fact(n):
    res = 1 
    for i in range(2, n + 1):
        res *= i
    return res

def answer(n):
    result = 0
    precomputing = {i:fact(i) for i in range(10)}
    for i in range(3, n):
        if i == sum([precomputing[int(x)] for x in str(i)]):
            result += i

    return result

print(answer(1000000))
