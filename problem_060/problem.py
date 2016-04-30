def eratosthene(n):
    l = range(2, int(n / 2 + 1))
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def find_closest_greater_unused_neighbor(l, x, used_neighbors):
    for value in l:
        if value > x and value not in used_neighbors:
            return (value, value - x)

def increasing_sum_subset(l, subset_size):
    current_subset = set(l[:subset_size])
    current_sum = sum(current_subset)
    maximum_sum = sum(l[subset_size:])
    
    yield current_subset, current_sum
    while not current_sum == maximum_sum:
        closest_next_values = {x : find_closest_greater_unused_neighbor(l, x, current_subset) for x in current_subset}
        list_closest = list(closest_next_values.items())
        list_closest.sort(key= lambda x: x[1][1])
        old_value, (new_value, diff) = list_closest[0]
        current_subset.remove(old_value)
        current_subset.add(new_value)
        current_sum += diff
        yield current_subset, current_sum
        

if __name__ == '__main__':
    primes = list(eratosthene(15))
    primes.sort()
    print("primes:", primes)
    for subset in increasing_sum_subset(primes, 3):
        print(subset)
