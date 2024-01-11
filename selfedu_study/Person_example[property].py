from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, age: int, passport: str, weight: float):
        self.verify_fio(fio)
        # self.verify_age(age)
        # self.verify_pasport(passport)
        # self.verify_weight(weight)

        self.__fio = fio  # str
        self.age = age  # int 14 <= fio <= 120
        self.passport = passport  # format xxxx xxxxxx, where (x: int) == (0 <= int <= 9)
        self.weight = weight  # float > 20.0 kg

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
        if type(age) != int or 14 > age or age > 120:
            raise TypeError("Возраст должен быть от 14 до 120 в цифрах")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            return TypeError("Вес должен быть вещественным числом от 20 и выше")

    @classmethod
    def verify_pasport(cls, passport):  # с хера не работает класс как исключение! наверное не вызвал! потом решу!
        if type(passport) != str:
            raise TypeError("Паспорт должен быть строкой")
        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Ссерия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_pasport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


x = Person("Ялалтдинов Амирам Мухарьямович", 27, '4457 365678', 78.7)
x.fio = 'Ялаев Филюс Мулланурович'
x.age = 29
x.passport = '1111 666664'
x.weight = '85'
print(x.__dict__)