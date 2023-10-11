spisok = [input() for _ in range(int(input()))]

out = [y for i, y in enumerate(spisok) if y not in spisok[:i]]
print(*out, sep='\n')







# out = [x for i, x in enumerate(spisok) if x not in spisok[:i]]
# print(out)
