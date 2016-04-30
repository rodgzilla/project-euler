f = open('p022_names.txt', 'r')
s = f.read()
list_names = s.split(',')
list_names = [name[1:-1] for name in list_names]
list_names.sort()

print(sum([(i + 1) * sum([ord(letter) - ord('A') + 1 for letter in name]) for i, name in enumerate(list_names)]))
