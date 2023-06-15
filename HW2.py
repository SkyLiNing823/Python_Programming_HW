L = [10, 20, 30, 'ABC', '123', '456']

# 以下請填入你的程式
first_part_length = int(len(L)) - int((len(L)/2))
second_part_length = int(len(L))
L = L[first_part_length:first_part_length +
      second_part_length]+L[:first_part_length]
# 以上請填入你的程式

print(L)
