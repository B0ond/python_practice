# # нужно сделать стак у которого есть методы push(вносим в данные), pop(удаляем и возвращаем),
# # top(верхнее значение), min_value(минимальное значение)
#
# from array import array
#
#
# class Stack:
#     def __init__(self):
#         self.data = []
#         self.min_data = []
#
#     def push(self, num):
#         self.data.append(num)
#         if not self.min_data or num <= self.min_data[-1]:
#             self.min_data.append(num)
#
#     def pop(self):
#         if not self.data:
#             return None
#         removed_element = self.data.pop()
#         if removed_element == self.min_data[-1]:
#             self.min_data.pop()
#         return removed_element
#
#     def top(self):
#         if self.data:
#             return self.data[-1]
#
#     def min_value(self):
#         if self.min_data:
#             return self.min_data[-1]
#
#
# out = Stack()

def modif_str(stroka:str):
    return stroka[1:-1]


print(modif_str('A1234567A'))