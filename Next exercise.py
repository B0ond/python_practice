# person = {}
# data = "summa, faba, 2, 4, 5, 67, -2, -3, data_format, zz"
# sort_data = data.split(',')
# p1 = '1: data'
# p2 = '2: sort_data'
# p3 = '3: join(sort_data)'
# p4 = '4: join(data)'
# max_p_len = max(len(p1), len(p2), len(p3), len(p4))
# print(max_p_len)
# print(p1, '-' * max_p_len, data)
# print(p2, '-' * max_p_len, sort_data)
# print(p3, '-' * max_p_len, ''.join(sort_data))
# print(p4, '-' * max_p_len, ''.join(data))
# in top a legacy code

import random

dataformat = ['asdasd', 'bbbbbbbbb', 'cccccccccc', 'ddddddddddd', 'eeeeeeeeeeeee']
newobject = random.randint(1, 10) dataformat.append(newobject)
data = "summa, faba, 2, 4, 5, 67, -2, -3, data_format, zz"

sort_data = data.split(',')
texFormatting = ['data', 'sort_data', 'join(data)', 'join(sort_data)', 'bacbacbabadadadadфывфывф']
count_text_format = len(texFormatting)
data_format = [data, sort_data, ''.join(sort_data), ''.join(data), sort_data]
count_data_format = len(data_format)
print('Введите 0 что бы не менять список, 1 для изменения списка')
flag = int(input())
try:
    if flag == 0:
        print()
    else:
        new_text = input('Введите новые данные для текста:')
        new_format = input()

if count_text_format != count_data_format:
    print('add correct text and data')

max_p_len = max(len(name) for name in texFormatting)
for i in range(count_text_format):
    print(texFormatting[i], '-' * (10 + (max_p_len - len(texFormatting[i]))), data_format[i])

print('count of texFormatting elements', len(texFormatting))
print('the type of texFormatting is:', type(texFormatting))

