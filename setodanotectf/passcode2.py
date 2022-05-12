data = ['18', '1f', '4', '79', '4f', '5a', '4', '18', '1a', '1b', '1e']

for i in data:
  print(chr(int(i, 16) ^ int('2a', 16)), end='')
print()