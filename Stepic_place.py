def some_foo(int_list):
        return sorted(int_list, key=lambda x: x == 0)

x = [0, 4, 1, 0, 6, 8, 9, 4, 6, 234, 465, 456, 456, 48, 9, 23, 1, 0]
print(some_foo(x))



# def sort_zero_to_end(digits):
#     zero_digit = []
#
#     for digit in digits:
#         if digit == 0:
#             zero_digit.append(digit)
#             digits.remove(digit)
#     digits.extend(zero_digit)
#     return  digits
# x = [0, 4, 1, 0, 6, 8, 9, 4, 6, 234, 465, 456, 456, 48, 9, 23, 1, 0]
# print(sort_zero_to_end(x))
