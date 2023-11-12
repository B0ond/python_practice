psw = input()
seq = psw.split(":")
seq = [int(el) for el in seq]
print(seq)
