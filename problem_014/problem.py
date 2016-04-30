def compute_collatz_sequence(start):
    sequence = [start]
    x = start
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    return sequence

def find_longest_collatz_sequence(largest_starting_value):
    best_starting_value = 0
    max_sequence_length = 0

    for i in xrange(1, largest_starting_value):
        seq = compute_collatz_sequence(i)
        if len(seq) > max_sequence_length:
            max_sequence_length = len(seq)
            best_starting_value = i

    return best_starting_value, max_sequence_length

if __name__ == '__main__':
    import sys
    print find_longest_collatz_sequence(int(sys.argv[1]))
