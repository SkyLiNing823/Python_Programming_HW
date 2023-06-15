dict = {}
I = input().split()
for i in I:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
L = sorted(dict.items(), key=lambda x: x[1])
for key, value in L:
    print(f'{key}: {value}')
