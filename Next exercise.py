n = int(input())
nx = n
if n % 2 > 0:
    for i in range(1, n // 2 + 1):
        print("*" * i)
    for j in range(nx // 2 + 1, 0, -1):
        print("*" * j)
else:
    print('Not a odd number')