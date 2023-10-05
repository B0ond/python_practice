vowels = ['num', 'e', 'i', 'o', 'u']
word = input('Insert num word: ')
found = []
counter = {}
for letter in word:
    if letter in vowels:
        counter[letter] = counter.get(letter, 0) + 1
        found.append(letter)
print(set(found))

#         if letter not in found:
#             found.append(letter)
# for i, j in zip(found, counter.count(k) for k in counter):
#     print(i, j)