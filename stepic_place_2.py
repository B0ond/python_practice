class Calculator:
    HEX_ALFABET = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    @classmethod
    def check_value(cls, x):
        cls.x = x
        if not isinstance(x, int) or x < 0:
            return False

    def convert_to_2_digit(self, decimal):
        if self.check_value(decimal):
            raise ValueError('Введенное число должно быть целым положительным числом и больше 0!')
        out = []
        while decimal > 0:
            binary = decimal % 2
            out.append(binary)
            decimal //= 2
        return ''.join(map(str, out[::-1]))

    def convert_to_16_digit(self, decimal):
        if self.check_value(decimal):
            raise ValueError('Введенное число должно быть целым положительным числом и больше 0!')
        out = []
        while decimal > 0:
            hexadecimal = decimal % 16
            out.insert(0, self.HEX_ALFABET[hexadecimal])
            decimal //= 16
        return ''.join(out)


out_line = Calculator()
while True:
    # try:
    name = input("Выберите в какую систему перевести десятичное число 'bin/hex': ")
    if name == 'bin':
        x = int(input('Введите число: '))
        print(f'Число {x} в двоичной системе будет равно {out_line.convert_to_2_digit(x)}')
    elif name == 'hex':
        x = int(input('Введите число: '))
        print(f'Число {x} в шестнадцатеричной системе будет равно {out_line.convert_to_16_digit(x)}')
    else:
        print('Введите bin или hex')

