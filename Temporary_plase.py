a = {'name'}
b = {'name', 'age'}
c = {'name', 'age', 1, 2, 3.5}
d = {'name':'Avgust', 'age':65}
e = {'name':'Avgust', 'age':88, 1:34, 2:45, 3.5:56}
list_of_sets = [a, b, c, d, e]
names = ['a', 'b', 'c', 'd', 'e']
for i, item in enumerate(list_of_sets):
    print(names[i], type(item))
    # i +=1
# i = 0
# for item in list_of_sets:
#     print(names[i], type(item))
#     i +=1
