#a5+b5+c5+d5 =e5
from datetime import datetime
start_time = datetime.now()
summa = 0
power = 5
loos = 0
found_solution = False
for a in range(1, 151):
    if found_solution == True:
        break
    for b in range(1, 151):
        if found_solution == True:
            break
        for c in range(1, 151):
            if found_solution == True:
                break
            for d in range(1, 151):
                sum = a ** power + b ** power + c ** power + d ** power
                e = int(sum ** (0.2))
                if sum == e ** 5:
                    print('a =', a, 'b =', b, 'c =', c, 'd =', d,'e =', e)
                    print('Искомое число =', a+b+c+d+e)
                    found_solution = True
                    break
                else:
                    loos += 1
end_time = datetime.now()
print("Неудачных решений =", loos)
print('Duration: {}'.format(end_time - start_time))