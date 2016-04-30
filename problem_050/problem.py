def eratosthene(n):
    l = range(2, n / 2 + 1)
    primes = set(range(2, n))
    
    for number in l:
        if number in primes:
            current_multiple = 2 * number
            while current_multiple < n:
                if current_multiple in primes:
                    primes.remove(current_multiple)
                current_multiple += number

    return primes

def consecutive_prime_sum(max_value):
    primes = eratosthene(max_value)
    print "era fini"
    prime_list = list(primes)
    prime_list.sort()
    print "sort fini"
    len_longest_seq = []

    for i in range(len(prime_list)):
        if i % 100 == 0:
            print "prime", i
        longest_seq_len = 0
        current_prime_sum = prime_list[i]
        j = 1
        while i + j < len(prime_list) and current_prime_sum < max_value:
            current_prime_sum += prime_list[i + j]
            if current_prime_sum in primes:
                longest_seq_len = j + 1
            j += 1
        len_longest_seq.append(longest_seq_len)

    index_max = 0
    for i in range(len(len_longest_seq)):
        if len_longest_seq[i] > len_longest_seq[index_max]:
            index_max = i

    print prime_list[index_max: index_max + len_longest_seq[index_max]]
    print len_longest_seq[index_max]

    return sum(prime_list[index_max: index_max + len_longest_seq[index_max]])

if __name__ == '__main__':
    print consecutive_prime_sum(10000000)
