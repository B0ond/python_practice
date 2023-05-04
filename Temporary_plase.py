n = int(input())
max_digit = -1                        #0 делится на любое натуральное чилсо поэтому граница будет от -1
while n > 0:                          #пока не кончится
    last_digit = n % 10               #переименовал переменную по PeP
    if last_digit % 3 == 0:
        if last_digit > max_digit:    #для перезаписси условия недо поставить >
            max_digit = last_digit    # мы приравниваем переменную max_digit к последней а не наоборот
    n = n // 10                       #убераем вычисленное число для что бы начать следующее
if max_digit == -1:                   #нсли неменяется установленный msx_digit то пишем NO
    print('NO')
else:
    print(max_digit)