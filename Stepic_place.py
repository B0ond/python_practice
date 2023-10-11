spisok = [input() for _ in range(int(input()))]
requests = [input() for _ in range(int(input()))]

out = []
for i in spisok:
    if requests.lower() in i.lower():
        print(i)
