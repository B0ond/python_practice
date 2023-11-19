def is_valid(stroka):
    try:
        if 1 <= int(stroka) <= 100:
            return True
        else:
            return False
    except ValueError:
        return False

x = input()
print(is_valid(x))