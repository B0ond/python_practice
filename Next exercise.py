n = int(input())
rsoult = 0
for i in range(2, n+1):
    if rsoult == n % i:
        print(rsoult)