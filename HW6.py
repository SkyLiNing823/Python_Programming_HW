n = int(input())
i = 2
while(i**2 <= n):
    if(n % i == 0):
        break
    i += 1
if(i**2 <= n):
    print('no')
else:
    print('yes')
