phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(1):
    plist.pop(i)
plist.remove("'")
for _ in range(4):
    plist.pop()
t = plist.pop(2)
p = plist.pop(3)
plist.insert(3, t)
plist.insert(5, p)
print(t, p)



new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

#target = 'on tap'
