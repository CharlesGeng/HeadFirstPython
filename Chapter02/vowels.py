vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Please input a word:')
found = []

for c in word:
    if c in vowels:
        if c not in found:
            found.append(c)

for c in found:
    print(c)