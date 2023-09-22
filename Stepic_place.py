#a5+b5+c5+d5 =e5
from datetime import datetime
start_time = datetime.now()
summa = 0
power = 5
loos = 0
wins = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                loos += 1
                if a**power + b**power + c**power == d**power:
                    wins += 1
                    # print('a =', a, 'b =', b, 'c =', c, 'd =', d, end=' ')
                break
summa = a+b+c+d
print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, end='\n')
print('Верных решений = ', wins)
print('Неверных решений = ', loos)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
#print('сумма верных решений = ', summa)
