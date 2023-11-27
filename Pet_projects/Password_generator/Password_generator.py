import secrets

#для корркетного запуска программы устновите модуль art, либо закоментить/удалить помеченну строчку в коде
from art import tprint

def get_input(prompt):
    """возвращает int число, цикл бесконечен до ввода числа"""
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print('число не может быть отрицательным или нулем!')

def yes_or_not(prompt):
    """возвращает True если ввели 'Y' or 'y' и False если 'N' or 'n' """
    while True:
        user_input = input(prompt)
        if user_input in ('Y', 'y'):
            return True
        if user_input in ('N', 'n'):
            return False
        print('Введите "Y" да или "N" нет')


def generate_password(length, chars):
    return ''.join(secrets.choice(chars) for _ in range(length))


def get_word_form(number):
    """меняет склонение слова <пароль>"""
    if 11 <= number <= 19:
        return 'паролей'
    if number % 10 == 1:
        return 'пароль'
    if number % 10 in (2, 3, 4):
        return 'пароля'
    return "паролей"
def main():
    tprint('Created by <<<Amiram>>>')  # заставка (если не установлен модуль art закоментить/удалить строку)

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    indistinct_characters = 'il1Lo0Oo'

    number_of_pass = get_input('Введите количество паролей для генерации: ')
    len_of_pass = get_input('Введите длину каждого пароля: ')
    print()

    # chars, yes_or_not, digits, uppercase_letters, lowercase, punctuation, indistinct,
    while True:
        count = 0
        include_digit = yes_or_not('Включать ли цифры Y/N: ')
        includ_upper = yes_or_not('Включать ли прописные буквы Y/N: ')
        includ_lower = yes_or_not('Включать ли строчные буквы Y/N: ')
        includ_symbols = yes_or_not('Включать ли символы Y/N: ')
        indistinct = yes_or_not('Убрать из генерации неоднозначные символы Y/N: ')
        if include_digit:
            chars += digits
            count += 1
        if includ_upper:
            chars += uppercase_letters
            count += 1
        if includ_lower:
            chars += lowercase_letters
            count += 1
        if includ_symbols:
            chars += punctuation
            count += 1
        if indistinct:
            translate_table_indistinct = str.maketrans('', '', indistinct_characters)  # maketrans создает таблицу словарь со значениями символов по табице ASKII
            chars = chars.translate(translate_table_indistinct)  # translate превращает обратно в буквы
        if count <= 0:
            print()
            print('Пожалуйста включите хотя бы один набор паролей!')
            print()
            continue
        break
    #<<<начало выбора склонений
    text_genereted_word = 'сгенерировано'
    text_symbol = 'символов'
    if number_of_pass % 10 == 1:
        text_genereted_word = 'сгенерирован'
    if len_of_pass % 10 == 1:
        text_symbol = 'символ'
    #>>>конец выбора склонений

    print()
    print('*'*100)
    print('<<<Начало генерации паролей со следующей строки>>>')
    for _ in range(number_of_pass): #генерация паролей
        print(generate_password(len_of_pass, chars))
    print(f'<<<Успешно {text_genereted_word} {number_of_pass} {get_word_form(number_of_pass)} длиной {len_of_pass} {text_symbol}>>>')

if __name__ == '__main__':
    main()
