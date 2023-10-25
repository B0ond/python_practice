encrypted_string = input().split()
print(*[i[1:]+i[:1]+'ки' for i in encrypted_string])
