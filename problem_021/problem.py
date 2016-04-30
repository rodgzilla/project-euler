def divisors(n):
    return [i for i in range(1, n) if n%i == 0]

def is_amicable_couple(a):
    b = sum(divisors(a))
    if a != b and sum(divisors(b)) == a:
        return True
    return False

def amicable_number_list(max_value):
    return [i for i in range(1, max_value + 1) if is_amicable_couple(i)]

if __name__ == '__main__':
    print sum(amicable_number_list(10000))
