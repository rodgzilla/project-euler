def count_powerful_digits(digit_number):
    lower_bound = 10 ** (digit_number - 1)
    upper_bound = 10 ** digit_number
    i = 1
    res = 1
    count = 0
    
    while res < upper_bound:
        if res >= lower_bound:
            count += 1
        i += 1
        res = i ** digit_number

    return count

print(sum([count_powerful_digits(i) for i in range(1, 100)]))
