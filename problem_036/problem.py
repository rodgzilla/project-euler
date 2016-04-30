def is_palindromic_both_bases(x):
    def is_palindromic(s):
        for i in range(len(s) / 2):
            if s[i] != s[-i - 1]:
                return False
        return True
    return is_palindromic(str(x)) and is_palindromic("{0:b}".format(x))

def compute_sum(n):
    return sum([x for x in range(1, n + 1) if is_palindromic_both_bases(x)])

if __name__ == '__main__':
    print compute_sum(1000000)
