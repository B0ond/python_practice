x = input()


start = x.find('h')
end = x.rfind('h')

rep_x = x[start+1:end]
rev_x = rep_x[::-1]

print(x.replace(rep_x, rev_x))
