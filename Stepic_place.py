def is_palindrome(num):
    return num == num[::-1]

def is_prime(num):
    num = int(num)
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_even(num):
    num = int(num)
    if num % 2 == 0:
        return True

def good_pass(paswrd):
    out = False
    indx = []
    count = 0

    for i in range(len(paswrd)):
        if paswrd[i] == ':':
            count += 1
            indx.append(i)
            if count > 2:
                return False
    if count == 2:
        if is_palindrome(paswrd[:indx[0]]):
            out = True
        else:
            return False
        if is_prime(paswrd[indx[0]+1:indx[1]]):
            out = True
        else:
            return False
        if is_even(paswrd[indx[1]+1:]):
            out = True
        else:
            return False
    if out == True:
        return True



num = input()


print(good_pass(num))