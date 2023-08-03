import random

dataformat = ['asdasd', 'bbbbbbbbb', 'cccccccccc', 'ddddddddddd', 'eeeeeeeeeeeee']
newobject = random.randint(1, len(dataformat))
dataformat.append(dataformat[newobject])
print(dataformat)
