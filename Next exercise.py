# put your python code here
total = 0
for x in range(1, 10):
    for y in range(1, 20):
        for j in range(1, 200):
            if 10 * x + 5 * y + 0.5 * j == 100:
                total += 1
                print('Быки', x, 'коровы', y, 'телята', j )
                print('Общее количество решений',total)