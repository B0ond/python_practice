# person = {}
# data = "summa, faba, 2, 4, 5, 67, -2, -3, ff, zz"
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


data = "summa, faba, 2, 4, 5, 67, -2, -3, ff, zz"
sort_data = data.split(',')
p1 = '1: data'
p2 = '2: sort_data'
p3 = '3: join(sort_data)'
p4 = '4: join(data)'
pp = [p1, p2, p3, p4]
ff = [data, sort_data, ''.join(sort_data), ''.join(data)]
max_p_len = max(len(p1), len(p2), len(p3), len(p4))
abc = [print(pp[i], '-' * max_p_len + (max_p_len - pp[i]), ff[i]) for i in range(4)]

# print(p1, '-' * max_p_len, data)
# print(p2, '-' * max_p_len, sort_data)
# print(p3, '-' * max_p_len, ''.join(sort_data))
# print(p4, '-' * max_p_len, ''.join(data))
