from functools import reduce
from itertools import permutations

def number_set_with_formula(borne_inf, borne_sup, formula):
    i = 1
    current_number = formula(1)
    numbers_set = set()

    while current_number < borne_sup:
        if current_number >= borne_inf:
            numbers_set.add(current_number)
        i += 1
        current_number = formula(i)
    
    return numbers_set

def compute_dicts(number_sets):
    set_indices = list(range(len(number_sets))) + [0]
    dict_list = []
    for i in range(len(set_indices) - 1):
        d = {}
        for number_s1 in number_sets[set_indices[i]]:
            suffix = number_s1 % 100
            if suffix < 10:
                continue
            valid_next = set([number_s2 for number_s2 in number_sets[set_indices[i + 1]] if number_s2 // 100 == suffix])
            if len(valid_next) > 0:
                d[number_s1] = valid_next
        dict_list.append(d)
    return dict_list

def compute_solution(dict_list):
    set_indices = list(range(len(dict_list))) + [0]

    for i in range(len(set_indices) - 1):
        possible_keys_set = reduce(set.union, dict_list[set_indices[i]].values(), set())
        keys_next_dict = set(dict_list[set_indices[i + 1]])
        for key in keys_next_dict - possible_keys_set:
            dict_list[set_indices[i + 1]].pop(key)

    if len(dict_list[0]) != 0 and \
       any([number in dict_list[1] for values in dict_list[0].values() for number in values]):
        try:
            for first_number in dict_list[0]:
                for value_0 in dict_list[0][first_number]:
                    for value_1 in dict_list[1][value_0]:
                        for value_2 in dict_list[2][value_1]:
                            for value_3 in dict_list[3][value_2]:
                                for value_4 in dict_list[4][value_3]:
                                    if value_4 % 100 == first_number // 100:
                                        print(first_number + value_0 + value_1 + value_2 + value_3 + value_4)
                                        return True
        except:
            pass
    return False

if __name__ == '__main__':
    borne_inf = 1000
    borne_sup = 10000
    number_sets = [number_set_with_formula(borne_inf, borne_sup, lambda x: (x * (x + 1)) // 2),
                   number_set_with_formula(borne_inf, borne_sup, lambda x: x * x), 
                   number_set_with_formula(borne_inf, borne_sup, lambda x: ((x * (3 * x - 1)) // 2)),
                   number_set_with_formula(borne_inf, borne_sup, lambda x: x * (2 * x - 1)),
                   number_set_with_formula(borne_inf, borne_sup, lambda x: (x * (5 * x - 3)) // 2),
                   number_set_with_formula(borne_inf, borne_sup, lambda x: x * (3 * x - 2))]
    for ns in permutations(number_sets):
        dict_list = compute_dicts(ns)
        res = compute_solution(dict_list)
        if res:
            exit()
