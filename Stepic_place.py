spisok = [input() for _ in range(int(input()))]
request = input()
out = []

for i in spisok:
    print('request lower ==', request.lower())
    print('i.lower ========', i.lower())
    print('-----------------------------')
    if request.lower() in i.lower():
        print(i)








