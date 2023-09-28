a, b = int(input()), int(input())
while a < 2:
    a += 1
prime = 0
for i in range(a, b+1):
    if i == 2 or i == 3 or i == 5 or i == 7 or i == 11:
        print(i)
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % (i ** (0.2)) != 0:
        print(i)
