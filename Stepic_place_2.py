stroka = input().split()

deleted_ki = ([i[:-2] for i in stroka if len(i) > 1])
decoded_text = ([i[-1]+i[:-1] for i in deleted_ki if len(i) > 1])

print(*decoded_text)


# stroka = input().split()
# first_str = [i[0] for i in stroka]
# print(first_str)
#
# a ='животное'
# print(a[:3])