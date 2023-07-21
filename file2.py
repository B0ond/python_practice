numbers = [int(input()) for i in range(4)]
if all(x == numbers[0] for x in numbers):
    print('All numbers a same')
else:
    num_count={}
    for num in numbers:
        num_count[num] = num_count.get(num,0)+1
        print(num_count)
    max_count = max(num_count.values())
    print(f"The number if identical numbers is:{max_count}")