data = [65, 127, 89, 80, 182, 160, 183, 182, 89, 118, 119, 116, 177, 189, 177]
for i in range(len(data)):
  data[i] ^= 35

for i in range(len(data)):
  A_0 = data[i]
  if(A_0 == 107 or A_0 == 117 or A_0 == 108 or A_0 == 102 or A_0 == 98):
    data[i] += 3

for i in range(len(data)):
  data[i] ^= 21

for i in range(len(data)):
  data[i] -= 32

for i in range(len(data)):
  data[i] ^= 19

for i in data:
  print(chr(i), end='')