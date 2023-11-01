def find_all(target, symbol):
    target_t = target
    x = []
    while symbol in target_t:
        y = target_t.find(symbol)
        target_t = target_t[:y] + '0' + target_t[y+1:]
        x.append(y)
    return x

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

