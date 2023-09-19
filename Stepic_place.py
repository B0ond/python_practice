for x in range(1, 10):
    for y in range(1, 18):
        for z in range(2, 99, 2):
            if (x*10 + y*5 + z*0.5 == 100) and (x + y + z == 100):
                print(x, y, z)