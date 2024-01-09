from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, age: int, passport: str, weight: float):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_weight(weight)

        self.__fio = fio  # str
        self.__age = age  # int 14 <= fio <= 120
        self.__passport = passport  # format xxxx xxxxxx, where (x: int) == (0 <= int <= 9)
        self.__weight = weight  # float > 20.0 kg

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for letter in f:
            if len(letter) < 1:
                raise TypeError("В ФИО должна быть хотя бы 1 буква")
            if len(letter.strip(letters)) != 0:
                raise TypeError("В ФИО можно использвоать буквенные символы и девис")

    # @classmethod
    # def verify_age(cls, age):
    #     if type(age) != int or 14 > age > 120:
    #         raise TypeError("Возраст должен быть от 14 до 120 в цифрах")

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) and 14 > age > 120:
            raise TypeError("Возраст должен быть от 14 до 120 в цифрах")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            return TypeError("Вес должен быть вещественным числом от 20 и выше")

    # @classmethod
    # def verify_pasport(cls, passport):


x = Person("Ялалтдинов Амирам Мухарьямович", 27, '44567 345678', 78.7)