import random

dataformat = ['asdasd', 'bbbbbbbbb', 'cccccccccc', 'ddddddddddd', 'eeeeeeeeeeeee']
cloneObject = dataformat
randomNum = random.randint(0, len(dataformat) - 1)
cloneObject.append(dataformat[randomNum])
print(randomNum, cloneObject, sep='\n')