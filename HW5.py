Input = input().split()
x = Input[0]
y = Input[1]
s1 = 0
s2 = 0
try:
    x = float(x)
    x = -x if x < 0 else x
except:
    s1 = 1
try:
    y = float(y)
    y = -y if y < 0 else y
except:
    s2 = 1
if(s1 == 0 and s2 == 0):
    print(x+y)
elif(s1 == 1 and s2 == 0):
    print(x+str(y))
elif(s1 == 0 and s2 == 1):
    print(x)
else:
    print(len(x)+len(y))
