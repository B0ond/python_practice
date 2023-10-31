def math_blck_mag(number, quntity):
    numeration = int(str(number) * quntity)
    significant = 0
    for i in range(quntity):
        significant += number
    return numeration/significant

print(math_blck_mag(5,4))

