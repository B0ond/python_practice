

chars = ''
while True:
    count = 0
    if validate[0]:
        chars += digits
        count += 1
    if validate[1]:
        chars += uppercase_letters
        count += 1
    if validate[2]:
        chars += lowercase_letters
        count += 1
    if validate[3]:
        chars += punctuation
        count += 1
    if count <= 0:
        print('Пожалуйста выберите хотя бы один тип ')
        validete_input()
        continue
    else:
        break