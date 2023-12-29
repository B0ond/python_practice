class Point:
    MAX_COORD = 100
    MIN_COORD = 0
    def __init__(self, x=0, y=0):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coords(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise  ValueError('Координаты должны быть числами')

    @classmethod
    def set_bound(cls, new_min_coord):
        cls.MIN_COORD = new_min_coord

    def get_coords(self):
        return self.__x, self.__y


pt = Point()

pt.set_coords(6, 5)
print(pt.get_coords())

pt = Point.set_bound(4)
print(pt.__dir__)