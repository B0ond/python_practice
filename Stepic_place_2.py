def convert_to_python_case(text):
    out = ''
    index = 0
    prev_char_is_upper = False
    while len(text) != index:
        if text[index].isupper():
            out += '_' + text[index]
        else:
            out += text[index]
        index += 1
    return out[1:].lower()


# считываем данные
txt1 = input()

# вызываем функцию
print(convert_to_python_case(txt1))