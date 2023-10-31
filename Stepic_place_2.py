stroka = input().split()

deleted_ki = ([i[:-2] for i in stroka if len(i) > 1])
decoded_text = ([i[-1]+i[:-1] for i in deleted_ki if len(i) > 1])

print(*decoded_text)
