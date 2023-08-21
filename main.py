# matrix = [
#     [1, 2, 3, 6, 7],
#     [22, 56, 76, 34, 34],
#     [2.5, 7.5, 7.2, 2.7, 4.4],
#     ['a', 'b', 'c', 'd', 'e']
# ]
matrix = [1, 2, 3, 6, 7]


transposed_matrix = [[transp[i] for transp in matrix]for i in range(4)]
print(transposed_matrix)