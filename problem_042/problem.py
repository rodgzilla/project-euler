letter_values = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1, 27)))
words = [word[1:-1] for word in open('p042_words.txt', 'r').read().split(',')]
triangle_numbers = set([n * (n + 1) // 2 for n in range(1, 200)])
print(len([word for word in words if sum([letter_values[letter] for letter in word]) in triangle_numbers]))
