def convert_to_python_case(text):
    for i in range(1,len(text)):
        if text[i].isupper():
            text = text[:i] + '_' + text[i].lower() + text[i+1:]
    text = text.lower()
    return text

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))