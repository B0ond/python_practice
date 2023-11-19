from random import randint
def random_num_found():
    print('Привет, я программа которую создал Амирам, он наделил меня способностью выбирать случайные числа!')
    print('Я загадала случайное чимсло от 1 до 100, попробуй отгадать минимум за7 попыток =) по окончании я покажу сколько попыток у тебя было)')
    number = randint(1, 100)
    counter = 0
    while True:
        figur_num = int(input())
        if figur_num > number:
            print('Слишком много, попробуйте еще раз')
            counter += 1
            continue
        elif figur_num < number:
            print('Слишком мало, попробуйте еще раз')
            counter += 1
        elif figur_num == number:
            print('Вы угадали, поздравляем!')
            counter += 1
            break
    print(f'потребовалось {counter} попыток')

random_num_found()