import secrets
from art import tprint

def get_input(prompt):
    """возвращает int число, цикл бесконечен до ввода числа"""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('введите пожалуйста число')
            continue

def yes_or_not(prompt):
    """возвращает True если ввели 'Y' or 'y' и False если 'N' or 'n' """
    while True:
        user_input = input(prompt)
        if user_input == 'Y' or user_input == 'y':
            return True
        elif user_input == 'N' or user_input == 'n':
            return False
        else:
            print('Введите "Y" да или "N" нет')


def generate_password(length, chars):
    """генератор паролей"""
    return ''.join(secrets.choice(chars) for _ in range(length))

def get_word_form(number):
    """меняет склонение слова <пароль>"""
    if 11 <= number <= 19:
        return 'паролей'
    elif number % 10 == 1:
        return 'пароль'
    elif number % 10 in (2, 3, 4):
        return 'пароля'
    else:
        return "паролей"
def main():
    tprint('Created by <<<Amiram>>>')  # заставка

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    indistinct_Characters = 'il1Lo0Oo'

    number_of_pass = get_input('Введите количество паролей для генерации: ')
    len_of_pass = get_input('Введите длину каждого пароля: ')

    include_digit = yes_or_not('Включать ли цифры Y/N ')
    includ_upper = yes_or_not('Включать ли прописные буквы Y/N ')
    includ_lower = yes_or_not('Включать ли строчные буквы Y/N ')
    includ_symbols = yes_or_not('Включать ли символы Y/N ')
    indistinct = yes_or_not('Убрать из генерации неоднозначные символы Y/N ')

    if include_digit:
        chars += digits
    if includ_upper:
        chars += uppercase_letters
    if includ_lower:
        chars += lowercase_letters
    if includ_symbols:
        chars += punctuation
    if indistinct:
        translate_table_indistinct = str.maketrans('', '',
                                                   indistinct_Characters)  # maketrans создает таблицу словарь со значениями символов по табице ASKII
        chars = chars.translate(translate_table_indistinct)  # translate превращает обратно в буквы
    print(f'<<<Успешно сгенерировано {number_of_pass} {get_word_form(number_of_pass)} длиной {len_of_pass} символов>>>')
    for i in range(number_of_pass):
        print(generate_password(len_of_pass, chars))

if __name__ == '__main__':
    main()