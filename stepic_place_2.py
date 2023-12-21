class Flat:
    """Класс квартир в микрорайоне залупинск"""
    street = 'Gorkogo'
    street_number = 7
    flat_number = 5
    floor = 3

    def set_cost(self, first, second):
        self.first = first
        self.second = second

    def get_cost(self):
        return (self.first, self.second)


pervichka_cena = Flat()
per = Flat()
per.set_cost(7000, 5000)
per_ret = per.get_cost()


pervichka_cena.set_cost(5000, 4500)
pervichka_return = pervichka_cena.get_cost()

print(*pervichka_return, list(per_ret))