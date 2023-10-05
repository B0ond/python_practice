num = int(input())
сounter = 0

for _ in range(num):
    stroka = input()
    if stroka.count('11') >= 3:
        сounter += 1
print(сounter)