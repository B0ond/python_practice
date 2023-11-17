from random import randint
def random_num_found():
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
