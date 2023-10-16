text = input().split()
reversed = []

text.sort()
reversed = [i for i in reversed(text)]
print(text, reversed)