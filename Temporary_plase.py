number = input() # вводим число как строку
if len(set(number)) == 1: # создаем множество из цифр числа и проверяем, состоит ли оно из одного элемента
    print("YES")
else:
    print("NO")