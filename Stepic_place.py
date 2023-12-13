print('найти ключь к шифру цезаря')
def find_key(text, abc, ABC, ):
    key_arr = []
    for key in range(1, len(text)-1):
        decoded_text = caesar_cipher_main(direction_variable, key, text, abc, ABC, mosch)