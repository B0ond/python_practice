# wins = 0
# lose = 0
# for a in range(1, 10):
#     for b in range(1, 18):
#         for c in range(1, 100):
#             for d in range(1, 100):
#                 for e in range(1, 150):
#                     if (a**5 + b**5 + c**5 + d**5 == e**5):
#                         wins += 1
#                     else:
#                         lose += 1
# print('Верных решений = ', wins)
# print("Недачных попыток = ", lose)
wins = 0
lose = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                e = (a ** 5 + b ** 5 + c ** 5 + d ** 5) ** (1/5)
                if e.is_integer():
                    wins += 1
                else:
                    lose += 1
print('Верных решений =', wins)
print('Недачных попыток =', lose)