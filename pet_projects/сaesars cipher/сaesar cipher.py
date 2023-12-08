def direction():
    """
    выбор шифровать или дешифровать с защитой от 'дурака'
    :return: True шифровать False дешифровать
    """
    while True:
        x = input('Выберите "Ш" шифровать или "Д" дешифровать: ')
        if x.lower() == 'ш':
            print('    >>>выбрано Шифрование')
            return True
        if x.lower() == 'д':
            print('    >>>выбрано дешифрование')
            return False
        print('Что то пошло не так 0_о: ')


def text_lang():
    """
    выбор языка c защитой
    :return: True русский False английский
    """
    while True:
        x = input('Язык алфавита "р" русский, "а" английский: ')
        if x.lower() == 'р':
            print('    >>>выбран Русский язык')
            return True
        if x.lower() == 'а':
            print('    >>>выбран Английский язык')
            return False
        print('Что то пошло не так 0_о: ')


def step(text_lang_variable):
    """
    шаг сдвига, с защитой
    :param text_lang_variable: True or False
    :return: int
    """
    if text_lang_variable is True:
        y = 32
    else:
        y = 26
    while True:
        if text_lang_variable is True:
            x = input('введите сдвиг (от 1 до 32): ')
            if x.isdigit() and 0 < int(x) <= 32:
                x = x.lstrip('0')
                print(f'    >>>шаг сдвига = {x}')
                return int(x)
        elif text_lang_variable is False:
            x = input('введите сдвиг (от 1 до 26): ')
            if x.isdigit() and 0 < int(x) <= 26:
                x = x.lstrip('0')
                print(f'    >>>шаг сдвига == {x}')
                return int(x)
        print(f'Число должно быть положительным целым в пределах от 1 до {y}')


def alfabet(text_lang_variable):
    if text_lang_variable is True:  # если True то Русский
        abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        ABC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif text_lang_variable is False:  # если False то Английский
        abc = 'abcdefghijklmnopqrstuvwxyz'
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return [abc, ABC]  # [0] строчные [1] заглавные

def caesar_cipher(direction_variable, text_lang_variable, step_variable, text):
    """
    функция шифрования
    :return: должна возвращать шифрованный или дешифрованный пароль
    """
    if text_lang_variable is True:  # если True то Русский
        abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        ABC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif text_lang_variable is False:  # если False то Английский
        abc = 'abcdefghijklmnopqrstuvwxyz'
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if direction_variable() is True:  # если True то шифровать
        for i in text:
            if i.isalpha() and i.islower():
                result +=  # тут остановился

    return direction_variable, text_lang_variable, step_variable, text


def main():
    """main function"""
    print("Caeser's cipher")
    direction_variable = direction()
    text_lang_variable = text_lang()
    step_variable = step(text_lang_variable)
    text = input('Введите текст: ')
    print(caesar_cipher(direction_variable, text_lang_variable, step_variable, text))


if __name__ == '__main__':
    main()
