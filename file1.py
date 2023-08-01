file = open('file.txt', encoding='utf-8')
text_length = len(file.read())
if text_length < 100:
    print('Number of characters less than 100, it is:', text_length)
else:
    print('there are more than 100 characters here, they are here', text_length, end='')
# print(file.read(100))

# for row in file:
#     for letter in row():
#         print(letter, end='')