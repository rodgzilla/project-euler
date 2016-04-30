import sys

def is_palindrome(n):
    string = str(n)
    for i in range(len(string) / 2):
        if string[i] != string[-i - 1]:
            return False

    return True

def largest_palindrome():
    palindrome_list = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            value = i * j
            if is_palindrome(value):
                palindrome_list.append(value)

    palindrome_list.sort(reverse = True)
    return palindrome_list[0]

if __name__ == '__main__':
    print largest_palindrome()
