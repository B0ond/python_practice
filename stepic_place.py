class Time:
    __DAY = 86400

    def __init__(self, second):
        if not isinstance(second, int):
            raise TypeError("Должно быть целое число")
        self.seconds = second

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
