
stroka1 = 'dddggg10oOhhh'
stroka2 = 'il1Lo0Oo'
translation_table = str.maketrans('', '', stroka2)
out = stroka1.translate(translation_table)
print(out)