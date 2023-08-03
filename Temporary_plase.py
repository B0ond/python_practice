ages, names = [int(input()) for _ in range(3)], 'Антон, Борис, Виктор'.split(', ')
print(ages)
if ages.count(max(ages)) == 1:
    print('ages1 ==:',ages)
    print(names[ages.index(max(ages))], 'старше всех')
elif ages.count(max(ages)) == 2:
    print('ages2 ==:',ages)
    index = ages.index(max(ages))
    print(names[index], 'и', names[ages.index(max(ages), index + 1)], 'старше всех')               #задаем перенос строки
elif ages.count(max(ages)) == 3:
    print('ages3 ==:',ages)
    print('Все одинаковы')