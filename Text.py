numbers = [int(input()) for _ in range(4)]
if all(x == numbers[0] for x in numbers):
    print("Все числа одинаковые")
else:
    num_count = {}
    for num in numbers:
        num_count[num] = num_count.get(num, 0) + 1
    max_count = max(num_count.values())
    print(f"Количество одинаковых чисел: {max_count}")