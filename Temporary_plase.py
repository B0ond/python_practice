cipher_shift = int(input())
shift_message = input()

for i in shift_message:
    shift_char = ord(i) - cipher_shift
    if  shift_char < 97:
        shift_char += 26
    print(chr(shift_char), end='')
