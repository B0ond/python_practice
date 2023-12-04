def declination(number_of_pass, len_of_pass):
    text_genereted_word = 'сгенерировано'
    text_symbol = 'символов'
    if number_of_pass % 10 == 1:
        text_genereted_word = 'сгенерирован'
    if len_of_pass % 10 == 1:
        text_symbol = 'символ'
    return [text_genereted_word, text_symbol]