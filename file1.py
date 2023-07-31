# s = [['moskva', 111], ['voronezh', 111], ['cypr', 111], ['samara', 999]]
# d = {
#     'moskva':777,
#     'voronezh':555,
#     'cypr':666
# }
# g = dict(moskva=717, voronezh=444)
# print(s, d, g, sep='\n')

person = {}
data = "summa, faba, 2, 4, 5, 67, -2, -3, ff, zz"
sort_data = data.split(',')
p1 = '1: data------------------'
p2 = '2: sort_data-------------'
p3 = '3: join(sort_data)-------'
p4 = '4: join(data)------------'
print(p1, data)
print(p2, sort_data)
print(p3, ''.join(sort_data))
print(p4,''.join(data))
# print(sort_data)