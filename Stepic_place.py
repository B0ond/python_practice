text = input().split()
reversed = []

text.sort()
reversed = [i for i in text]
reversed.reverse()
print(text, reversed)
