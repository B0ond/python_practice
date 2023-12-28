
from random import randint

the_right_num = 100
print('по умолчанию от 1 до 100, введите число если хотите поменять правую границу '+ '\n' +
 'на другое число, либо введите любую букву/символ если хотите оставить по умолчанию 100:')
x_default = input('Вввод: ')
try:
    if x_default.isdigit():
        the_right_num = int(x_default)
    else:
        print('установлены значения по умолчанию')
except ValueError:
    print('установлены значения по умолчанию')

random_num = randint(1, the_right_num)

print('Добро пожаловать в числовую угадайку ' +'введите число от 1 до ' + str(the_right_num))

def is_valid(stroka, the_right_num):
    """проверка на валидные вводимые данные"""
    try:
        if 1 <= int(stroka) <= the_right_num:
            return True
        else:
            return False
    except ValueError:
        return False
def check_input():
    """основной цикл проверки"""
    while True:
        user_num = input()
        if is_valid(user_num, the_right_num):
            return int(user_num)
        else:
            print('А может быть все-таки введем целое число от 1 до ' + str(the_right_num) + '?')
def end_function():
    """основная функция"""
    counter = 0
    while True:
        x = check_input()
        if x == random_num:
            print('Вы угадали, поздравляем!')
            counter += 1
            print('Попыток:', counter)
            break
        elif x <= random_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif x >= random_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        else:
            print('Error')
end_function()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
