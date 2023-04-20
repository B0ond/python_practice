n = int(input())
n2 = n
lastdigit = 0
quantity = 0
if n >= 10:
    while n:
        quantity += 1
        n = n // 10
second_digit = (n2 // 10 ** (quantity - 2) % 10)
print("Второе число = ", second_digit,"наше второе n = ", n2)
print("Количество = ", quantity)
print("Н деленый на 10 = ", n2 // 10)
print("количество -2 = ", quantity -2)
print("возведенное в степень", n2 // 10 ** 4)