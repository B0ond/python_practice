n = int(input())
max_digit = 0
for _ in range(n):
    last_digit = n % 10
    if last_digit % 3 == 0:
        if last_digit > max_digit:
            max_digit == last_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)