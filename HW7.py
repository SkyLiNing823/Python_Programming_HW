n = input()
L = list(n)
L = sorted(L)
i = len(L)
m = 0
while i > 0:
    m += int(L[len(L)-i])*10**(i-1)
    i -= 1
print(int(n)+m)
