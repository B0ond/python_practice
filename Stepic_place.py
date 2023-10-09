n = int(input())
spisok = []
stop_num = 0

for i in range(n):
    x = input()
    if len(x) > 2:
        spisok.append(x[1])
    else:
        continue
result_str = ''.join(spisok)

print(result_str)
