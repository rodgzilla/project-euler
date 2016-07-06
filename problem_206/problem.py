def is_valid(n):
    if n % 10 == 0 and \
       (n // 100) % 10 == 9 and\
       (n // 10000) % 10 == 8 and\
       (n // 1000000) % 10 == 7 and\
       (n // 100000000) % 10 == 6 and\
       (n // 10000000000) % 10 == 5 and\
       (n // 1000000000000) % 10 == 4 and\
       (n // 100000000000000) % 10 == 3 and\
       (n // 10000000000000000) % 10 == 2 and\
       (n // 1000000000000000000) % 10 == 1:
        return True
    return False

mini = 1010101010
maxi = 1389026623
for i in range(mini, maxi):
    if is_valid(i ** 2):
        print(i)
        break
