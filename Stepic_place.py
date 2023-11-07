def is_valid_triangle(side1, side2, side3):
    return 'YES' if a + b > c and a + c > b and b + c > a else 'NO'

# считываем данные
a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))
