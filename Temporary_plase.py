n = int(input())
while n % 10 >= n // 10 % 10 or n > 0:
    n = n // 10
print('Yes' if n < 10 else 'NO')
