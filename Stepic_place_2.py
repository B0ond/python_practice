def is_magic(date):
    date_list = date.split('.')
    day_and_moth = date_list[0] * date_list[1]
    if day_and_moth ==

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))