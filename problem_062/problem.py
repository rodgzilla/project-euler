def solve_problem(n, max_value):
    i = 0
    d = {}
    while i < max_value:
        string_i_to_the_n = str(i ** n)
        sorted_i_to_the_n = ''.join(sorted(string_i_to_the_n))
        if sorted_i_to_the_n not in d:
            d[sorted_i_to_the_n] = []
        d[sorted_i_to_the_n].append(i)
        i += 1

    potential_answer = []
    for k in d:
        if len(d[k]) == 5:
            potential_answer.append(d[k][0] ** n)
    potential_answer.sort()
    return potential_answer[0]

if __name__ == '__main__':
    print(solve_problem(3, 1000000))
