import secrets
from art import tprint #для корркетного запуска программы устновите модуль art, либо закоментить/удалить помеченну строчку в коде
def get_input(prompt):
    """
     цикл бесконечен до ввода числа
    :param prompt: str вводится описание
    :return: int
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print('число должно быть положительным целым больше 0!')


def yes_or_not(prompt):
    """
    возвращает True если ввели 'Y' or 'y' и False если 'N' or 'n'
    :param prompt: str вводится описание
    :return: True/False
    """
    while True:
        user_input = input(prompt)
        if user_input in ('Y', 'y'):
            return True
        if user_input in ('N', 'n'):
            return False
        print('Введите "Y" да или "N" нет')


def generate_password(length, chars):
    """
    length раз берет с chars символы, складывает и возращает полученную строку
    :param length: int длина пароля
    :param chars: str список букв к паролю
    :return: str
    """
    return ''.join(secrets.choice(chars) for _ in range(length))


def get_word_form(number):
    """
    меняет склонение слова <пароль>
    :param number: int
    :return: str
    """
    if 11 <= number <= 19:
        return 'паролей'
    if number == 1:
        return 'пароль'
    if number % 10 in (2, 3, 4):
        return 'пароля'
    return "паролей"


def validete_input():
    """
    возвращает список из 5 булевых значений
    :return:
    """
    status = [False, False, False, False, False]
    if yes_or_not('Включать ли цифры Y/N '):
        status[0] = True
    if yes_or_not('Включать ли прописные буквы Y/N '):
        status[1] = True
    if yes_or_not('Включать ли строчные буквы Y/N '):
        status[2] = True
    if yes_or_not('Включать ли символы Y/N '):
        status[3] = True
    if yes_or_not('Убрать из генерации неоднозначные символы Y/N '):
        status[4] = True
    return status


def create_chars_to_pass(digits, uppercase_letters, lowercase_letters, punctuation, indistinct_characters, chars):
    """
    Вносит нужные набры символов в строку chars
    :param digits: str
    :param uppercase_letters: str
    :param lowercase_letters: str
    :param punctuation: str
    :param indistinct_characters: str
    :param chars: str
    :return: str
    """
    while True:
        validate = validete_input()
        count = 0  # считаем количество наборов паролей
        if validate[0]:
            chars += digits
            count += 1
        if validate[1]:
            chars += uppercase_letters
            count += 1
        if validate[2]:
            chars += lowercase_letters
            count += 1
        if validate[3]:
            chars += punctuation
            count += 1
        if validate[4]:
            translate_table_indistinct = str.maketrans('', '',
                                                       indistinct_characters)  # maketrans создает таблицу словарь со значениями символов по табице ASKII
            chars = chars.translate(translate_table_indistinct)  # translate превращает обратно в буквы
        if count <= 0:  # если 0 то не один из наборов паролей не было введено
            print()
            print('Пожалуйста включите хотя бы один набор паролей!')
            print()
            continue
        return chars


def main():
    """
    Точка входа
    :return: ничего не возвращает
    """
    tprint('Created by <<<Amiram>>>')  # заставка (если не установлен модуль art закоментить строку)

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''  # строка куда будут вносистя буквы для пароля
    indistinct_characters = 'il1Lo0Oo'
    number_of_pass = get_input('Введите количество паролей для генерации: ')
    len_of_pass = get_input('Введите длину каждого пароля: ')
    print()
    chars = create_chars_to_pass(digits, uppercase_letters, lowercase_letters, punctuation, indistinct_characters, chars)

    # <<<начало выбора склонений
    text_genereted_word = 'сгенерировано'
    text_symbol = 'символов'
    if number_of_pass == 1:
        text_genereted_word = 'сгенерирован'
    if len_of_pass == 1:
        text_symbol = 'символ'
    # >>>конец выбора склонений

    print()
    print('*'*100)
    print('<<<Начало генерации паролей со следующей строки>>>')
    for _ in range(number_of_pass): #генерация паролей
        print(generate_password(len_of_pass, chars))
    print(f'<<<Успешно {text_genereted_word} {number_of_pass} {get_word_form(number_of_pass)} длиной {len_of_pass} {text_symbol}>>>')
if __name__ == '__main__':
    main()
