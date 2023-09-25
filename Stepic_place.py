a, b = int(input()), int(input())
max_summ = 0  #максимальная сумма
max_number = 0 #указывает на число с максимальной суммой делителей
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
            if count >= max_summ:
                max_summ == count
                max_number = i

print('count ====', count)
print('max_summ ==', max_summ)
print('max_number =', max_number)
