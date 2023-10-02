data = []
with open('file.txt', encoding='UTF-8') as file:
    for lines in file:
        data = lines.lstrip()
print(list(data))