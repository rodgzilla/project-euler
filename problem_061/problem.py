def number_set_with_formula(max_value, formula):
    i = 1
    current_number = 1
    numbers_set = set()

    while current_number < max_value:
        numbers_set.add(current_number)
        current_number = formula(i)
        i += 1
    
    return numbers_set

def are_cyclic(number_tuple):
    if str(number_tuple[-1])[-2:] != str(number_tuple[0])[:2]:
        return False

    return all((str(number_tuple[i])[-2:] == str(number_tuple[i + 1])[:2] for i in range(len(number_tuple) - 1)))
    
# def find_numbers(number_sets):
#     for number_tuple in ((a, b, c, d, e, f) \
#                          for a in number_sets[0] \
#                          for b in number_sets[1] \
#                          for c in number_sets[2] \
#                          for d in number_sets[3] \
#                          for e in number_sets[4] \
#                          for f in number_sets[5]):
#         if are_cyclic(number_tuple):
#             return number_tuple

def find_numbers(number_sets):
    res = set()
    for number_tuple in ((a, b, c) \
                         for a in number_sets[0] \
                         for b in number_sets[1] \
                         for c in number_sets[2]):
        res.add(number_tuple)

        if are_cyclic(number_tuple):
            return number_tuple
            
    return res

if __name__ == '__main__':
    borne = 10000
    number_sets = [\
                   number_set_with_formula(borne, lambda x: (x * (x + 1)) / 2), \
                   number_set_with_formula(borne, lambda x: x * x), \
                   number_set_with_formula(borne, lambda x: (x * (3 * x - 1) / 2)), \
                   number_set_with_formula(borne, lambda x: x * (2 * x - 1)), \
                   number_set_with_formula(borne, lambda x: (x * (5 * x - 3)) / 2), \
                   number_set_with_formula(borne, lambda x: x * (3 * x - 2)) \
               ]

    number_sets_4_digits = [set([x for x in s if x >= 1000]) for s in number_sets]
    print '\n'.join([str(x) for x in number_sets])
    res = number_sets_4_digits
    result = find_numbers(number_sets_4_digits)
    print (8128, 2882, 8281) in result
    print 8128 in number_sets_4_digits[0]
    print 2882 in number_sets_4_digits[1]
    print 8281 in number_sets_4_digits[2]
