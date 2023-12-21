class Cat():
    """описание кота"""
    def __init__(self, age, gender, breed, coat, eye_color, tail, weight, paws_color):
        """свойства кота"""
        self.age = age
        self.gender = gender
        self.breed = breed
        self.coat = coat
        self.eye_color = eye_color
        self.tail = tail
        self.weight = weight
        self.paws_color = paws_color


a = Cat(10, 'mail', 'maukun', 'balck', 'Blue', 32, 10, 'pig')

print(a.age)