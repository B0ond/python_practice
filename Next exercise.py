n = int(input())
n2 = n
lastdigit = 0
quantity = 0
if n >= 10:
    while n:
        quantity += 1
        n = n // 10
second_digit = (n2 // 10 ** (quantity - 2) % 10)
print("Второе число = ", second_digit,"n2 = ", n2)
print("Количество = ", quantity)
print("n2 // 10 = ", n2 // 10)
print("quantity -2 = ", quantity -2)
print("возведенное в степень", n2 // 10 ** quantity)
print("10 в степени которую указал", 10 ** quantity)