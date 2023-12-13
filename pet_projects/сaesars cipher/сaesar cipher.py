from spellchecker import SpellChecker

spell_en = SpellChecker(language='en')
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


def known_or_not():
    """
    True - ключь неизвестен/False - ключь известен
    :return: bool
    """
    while True:
        y = input('Вы знаете ключь шифрования ? д/н ')
        if y.lower() == 'н':
            print('    >>>выбран поиск ключа')
            return True
        if y.lower() == 'д':
            print('    >>>идите на следующий шаг')
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


def caesar_cipher_main(direction_variable, step_variable, text, abc, ABC, mosch):
    """
    функция шифрования
    :return:возвращает шифрованный или дешифрованный пароль
    """
    result = ''

    if direction_variable is True:  # если True то шифровать
        for i in text:
            if i.isalpha() and i.islower():
                result += abc[(abc.find(i) + step_variable) % mosch]
            elif i.isalpha() and i.isupper():
                result += ABC[(ABC.find(i) + step_variable) % mosch]
            else:
                result += i
    if direction_variable is False: # если False то дешифровать
        for i in text:
            if i.isalpha() and i.islower():
                result += abc[(abc.find(i) - step_variable) % mosch]
            elif i.isalpha() and i.isupper():
                result += ABC[(ABC.find(i) - step_variable) % mosch]
            else:
                result += i
    return result


def find_key(text, spell, direction_variable, abc, ABC, mosch):
    """рашифровка ключа"""
    key_arr = []
    for key in range(1, len(text)-1):  # хз почему от 1 до text-1
        decoded_text = caesar_cipher_main(direction_variable, key, text, abc, ABC, mosch)
        # в переменную входит расшифровка с клчюом key
        decoded_text_arr = decoded_text.split()  # делаем список из слов
        len_decoded_text_arr = len(decoded_text_arr)  # длина списка
        res = 0  # переменная для подсчета количества вхождений
        for j in range(len_decoded_text_arr):  # пробегаемся по словам
            if decoded_text_arr[j] in spell:  # если слово правильное орфографически
                res += 1                      # то записываем в res
        key_arr.append(res)  # создаем список из количества найденных правильных слов
    max_key = max(key_arr)
    return key_arr.index(max_key)


def main():
    """main function"""
    global step_variable, direction_variable, abc, ABC, mosch, spell
    print("Caeser's cipher")  # шапка

    known_or_not_variable = known_or_not()
    if known_or_not_variable is False:
        direction_variable = direction()  # направление свига
    text_lang_variable = text_lang()  # выбранный язык
    if text_lang_variable is True:  # если True то Русский
        abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        ABC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        spell = SpellChecker(language='ru')
        mosch = 32
    elif text_lang_variable is False:  # если False то Английский
        abc = 'abcdefghijklmnopqrstuvwxyz'
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        spell = SpellChecker(language='en')
        mosch = 26
    if known_or_not_variable is False:
        step_variable = step(text_lang_variable)  # сдвиг
    text = input('Введите текст: ')  # текст для обработки
    if known_or_not_variable is False:
        print(caesar_cipher_main(direction_variable, step_variable, text, abc, ABC, mosch))  #вывод функции шифрования
    else:
        print(f' ключь равен {1+find_key(text, spell, False, abc, ABC, mosch)}')

if __name__ == '__main__':
    main()
