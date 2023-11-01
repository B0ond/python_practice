my_str = "Привет, мир!"
# Индекс символа, который нужно заменить
index = 6
# Символ, которым нужно заменить
new_char = "*"

# Замена символа
my_str = my_str.replace(my_str[index], new_char, 1)

print(my_str)  # Выведет: Приве* мир!