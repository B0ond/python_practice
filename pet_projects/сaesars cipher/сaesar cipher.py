from spellchecker import SpellChecker
from art import tprint


def direction():
    """
    Выбор шифровать или дешифровать с защитой от 'дурака'
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
        y = 32  # если Русские алфавит-то y == 32
    else:
        y = 26  # если Англ алфавит-то y == 32
    while True:
        if text_lang_variable is True:  # если Рус
            x = input('введите сдвиг (от 1 до 32): ')
            if x.isdigit() and 0 < int(x) <= 32:
                x = x.lstrip('0')  # удаляет все начальные символы, указанные в аргументе -> (0)
                # это на случай если ввели 0005, 0012334 и т.д.
                print(f'    >>>шаг сдвига = {x}')
                return int(x)
        elif text_lang_variable is False:  # если Англ
            x = input('введите сдвиг (от 1 до 26): ')
            if x.isdigit() and 0 < int(x) <= 26:
                x = x.lstrip('0')  # удаляет все начальные символы, указанные в аргументе -> (0)
                print(f'    >>>шаг сдвига == {x}')
                return int(x)
        print(f'Число должно быть положительным целым в пределах от 1 до {y}')


def caesar_cipher_main(direction_variable, step_variable, text, abc, ABC, mosch):
    """
    Функция шифрования
    :return:возвращает шифрованный или дешифрованный пароль
    """
    result = ''  # пустой список для шифрованных букв

    if direction_variable is True:  # если True-то шифровать
        for i in text:
            if i.isalpha() and i.islower():  # если буква и если она маленькая
                result += abc[(abc.find(i) + step_variable) % mosch]  # вся МАГИЯ программы шифрования
            elif i.isalpha() and i.isupper():  # если буква и если она Большая
                result += ABC[(ABC.find(i) + step_variable) % mosch]
            else:
                result += i  # добавляем в пустой список шифрованные буквы
    if direction_variable is False: # если False-то дешифровать
        for i in text:  # каждую букву
            if i.isalpha() and i.islower():
                result += abc[(abc.find(i) - step_variable) % mosch]
            elif i.isalpha() and i.isupper():
                result += ABC[(ABC.find(i) - step_variable) % mosch]
            else:
                result += i
    return result


def find_key(text, spell, direction_variable, abc, ABC, mosch):
    """Расшифровка ключа"""
    key_arr = []
    for key in range(1, len(text)-1):  # хз почему от 1 до text-1
        decoded_text = caesar_cipher_main(direction_variable, key, text, abc, ABC, mosch)
        # в переменную входит расшифровка с ключом key
        decoded_text_arr = decoded_text.split()  # делаем список из слов
        len_decoded_text_arr = len(decoded_text_arr)  # длина списка
        res = 0  # переменная для подсчета количества вхождений
        for j in range(len_decoded_text_arr):  # пробегаемся по словам
            if decoded_text_arr[j] in spell:  # если слово правильное орфографически
                res += 1                      # то записываем в res
        key_arr.append(res)  # создаем список из количества найденных правильных слов
    max_key = max(key_arr)
    return key_arr.index(max_key)


def get_language_params(text_lang_variable):
    """
    Выбор алфавита, и максимального шага
    :param text_lang_variable: bool
    :return: str, str, SpellChecker, int
    """
    if text_lang_variable is True:  # если True-то Русский
        abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        ABC = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        spell = SpellChecker(language='ru')  # датасет сРусскими словами для сравнения правильности слов
        mosch = 32
    elif text_lang_variable is False:  # если False-то Английский
        abc = 'abcdefghijklmnopqrstuvwxyz'
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        spell = SpellChecker(language='en')  # датасет с Английскими словами для сравнения правильности слов
        mosch = 26
    return abc, ABC, spell, mosch


def main():
    """main function"""
    tprint(" Caesar's cipher - created by Amiram!")  # шапка

    direction_variable = direction()  # направление сдвига False дешифровать True шифровать
    text_lang_variable = text_lang()  # выбранный язык
    abc, ABC, spell, mosch = get_language_params(text_lang_variable)
    if direction_variable is True:  # False дешифровать True шифровать
        step_variable = step(text_lang_variable)
        text = input('Введите текст: ')  # текст для обработки
        print(caesar_cipher_main(direction_variable, step_variable, text, abc, ABC, mosch))  # вывод функции шифрования
    else:
        text = input('Введите текст: ')  # текст для обработки
        step_variable = 1+find_key(text, spell, False, abc, ABC, mosch)
        print(f'    >>>шаг сдвига = {step_variable}')
        print(caesar_cipher_main(direction_variable, step_variable, text, abc, ABC, mosch))  # вывод функции шифрования


if __name__ == '__main__':
    main()
