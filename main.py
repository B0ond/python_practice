n = int(input())

summa = 0
count = 0
myltiply = 1
avgarif = 0
firstdigit = 0
while n:
    lastdigit = n % 10
    summa += lastdigit        # Сумма цифр
    count += 1                # киличество цифр
    myltiply *= lastdigit     # произведение цифр
    avgarif = summa / count   # среднее арифметическое
    n = n//10
for i in range count



# первую цифру
# сумму первой и последней
print(summa)
print(count)
print(myltiply)
print(avgarif)
print(firstdigit)

