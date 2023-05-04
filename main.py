n = int(input())

summa = 0
count = 0
myltiply = 1
avgaif = 0
num_str = str(n)
firstdigit = num_str[0]                # первую цифру
last_digit = n % 10
while n:
    lastdigit = n % 10
    summa += lastdigit                 # Сумма цифр
    count += 1                         # киличество цифр
    myltiply *= lastdigit              # произведение цифр
    avgarif = summa / count            # среднее арифметическое
    n = n//10
summa_2 = int(firstdigit) + last_digit # сумму первой и последней

print(summa)
print(count)
print(myltiply)
print(avgarif)
print(firstdigit)
print(summa_2)

