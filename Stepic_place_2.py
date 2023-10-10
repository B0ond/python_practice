spisok = [input() for _ in range(int(input()))]

k = int(input())
for i in spisok:
    if i >= k:
        print(i[k-1], end='')