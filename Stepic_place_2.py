def is_magic(date):
    date_list = date.split('.')
    day_and_moth = int(date_list[0]) * int(date_list[1])
    if day_and_moth == int(date_list[2])%100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))