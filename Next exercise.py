# person = {}
# data = "summa, faba, 2, 4, 5, 67, -2, -3, formatting, zz"
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


data = "summa, faba, 2, 4, 5, 67, -2, -3, formatting, zz"
sort_data = data.split(',')

texFormatting = ['data', 'sort_data', 'join(data)', 'join(sort_data)', 'bacbacbabadadadadфывфывф']

print('count of texFormatting elements', len(texFormatting))
print('the type of texFormatting is:', type(texFormatting))

formatting = [data, sort_data, ''.join(sort_data), ''.join(data), sort_data]
max_p_len = max(len(name) for name in texFormatting)
for i in range(5):
    print(texFormatting[i], '-' * (10 + (max_p_len - len(texFormatting[i]))), formatting[i])

# table_dict = {p1: '1: data', p2: '2: sort_data', p3: '3: join(sort_data)', p4:'4: join(data)', p5: '5: bacbacbabadadadadфывфывф'}