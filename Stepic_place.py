number_of_rows = int(input())
spisok = [input() for _ in range(number_of_rows)]
requests = [input() for _ in range(int(input()))]

out = []
for i, j in enumerate(spisok):
    # for item in requests:
    #     if item in spisok:
    if all([item for item in requests if item in spisok]):
        print(j)


# for i in range(number_of_rows):
#     if requests[i].lower() in spisok[i].lower():
#         print(i)
