word = 'бутылок'
for beer_num in range(99, 0, -1):
    print(beer_num, word, "пива на стене")
    print(beer_num, word, "пива!")
    print("Возьми одну")
    print("Пусти по кругу")
    new_num = beer_num - 1
    if new_num == 0:
        print("Кончились бутылки пива на стене")
        exit()
    else:
        if 11 <= new_num <= 19:
            word = 'бутылок'
        elif new_num % 10 == 1:
            word = 'бутылка'
        elif new_num % 10 in (2, 3, 4):
            word = 'бутылки'
        else:
            word = "бутылок"
    print(new_num, word, "пива на стене")
    print()