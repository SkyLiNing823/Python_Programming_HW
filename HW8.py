x = input().split()
m = int(x[0])
n = int(x[1])
ans = []
count = 0
rev = False
for i in range(m):
    element = []
    for j in range(n):
        element.append(count)
        count += 1
    if(rev):
        element.reverse()
        rev = False
    else:
        rev = True
    ans.append(element)
print(ans)
