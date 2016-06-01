def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

jan = mar = may = jul = aug = oct = dec = tuple(range(1, 32))
apr = jun = sep = nov = tuple(range(1, 31))
feb_normal = tuple(range(1, 29))
feb_leap = tuple(range(1, 30))
century = [jan + (feb_leap if is_leap_year(year) else feb_normal) +
           mar + apr + may + jun + jul + aug + sep + oct + nov + dec for year in
           range(1900, 2001)]

day = 0
res = 0
for i, year in enumerate(century):
    for date in year:
        if i != 0 and date == 1 and day == 6:
            res += 1
        day = (day + 1) % 7

print(res)

