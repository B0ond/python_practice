def found_number(number: str):
    numerator = ''
    denominator = 0
    for i in range(int(number)):
        numerator += '1'
        denominator += 1
    return int(numerator) / denominator

x = input()
print(found_number(x))