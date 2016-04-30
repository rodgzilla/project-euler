def compute_continued_fraction_reduction_aux_rec(n):
    if n == 0:
        return (1, 2)
    x, y = compute_continued_fraction_reduction_aux(n - 1)
    return (y, 2 * y + x)

def compute_continued_fraction_reduction_iter(n):
    x = 1
    y = 2

    for i in range(n - 1):
        x_tmp = x
        x = y
        y = 2 * y + x_tmp

    return (x, y)


def compute_continued_fraction_reduction(n):
    x, y = compute_continued_fraction_reduction_iter(n)
    return (3 * y + x, 2 * y + x)

if __name__ == '__main__':
    i = 0
    cnt = 0

    # for i in range(50):
    #     print (compute_continued_fraction_reduction(i))
    while i < 1000:
        x, y = compute_continued_fraction_reduction(i)
        if len(str(x)) > len(str(y)):
            cnt += 1
#            print (x,y)

        i += 1
    print(cnt)

    
