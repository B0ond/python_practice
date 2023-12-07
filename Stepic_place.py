print('шифр цезаря')
def direction():
    """
    выбор шифровать или дешифровать
    :return: True шифровать False дешифровать
    """
    x = input('Выберите "Ш" шифровать или "Д" дешифровать')
    if x.lower() == 'ш':
        return True
    if x.lower() == 'д':
        return False
    print('Введите "Ш" шифровать или "Д" дешифровать')


def text_lang():
    """
    выбор языка
    :return: True русский False английский
    """
    x = input('Язык алфавита "р" русский, "а" английский')
    if x.lower() == 'р':
        return True
    if x.lower() == 'а':
        return False
    print('Введите "р" русский, "а" английский')
def caesar_cipher():
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    upper_rus_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def main():



if __name__ == '__main__':
    main()