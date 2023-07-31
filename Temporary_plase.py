ages, names = [int(input()) for _ in range(3)], 'Антон, Борис, Виктор'.split(', ')
if ages.count(max(ages)) == 1:
    print(names[ages.index(max(ages))], 'старше всех')
elif ages.count(max(ages)) == 2:
    index = ages.index(max(ages))
    print(names[index], 'и', names[ages.index(max(ages), index + 1)], 'старше всех')               #задаем перенос строки
elif ages.count(max(ages)) == 3:
    print('Все одинаковы')