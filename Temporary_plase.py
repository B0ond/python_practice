vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
found = []
for letter in word:
    if letter in vowels:
        found.append(letter)
print(set(found))