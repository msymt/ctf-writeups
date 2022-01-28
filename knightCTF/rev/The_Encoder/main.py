import string

s = string.ascii_letters + string.punctuation + string.digits

local_10 = 1337
local_14 = 0
local_48 = "1412 1404 1421 1407 1460 1452 1386 1414 1449 1445 1388 1432 1388 1415 1436 1385 1405 1388 1451 1432 1386 1388 1388 1392 1462"
local_48 = local_48.split(" ")
flag = ""

def countChar(s):
  local_c = 0
  local_10 = 0
  while True:
    if len(s) == local_10:
      break
    if s[local_10] != 10:
      local_c += 1
    local_10 += 1
  return local_c

# str -> int
for i in range(len(local_48)):
  local_48[i] = int(local_48[i])

for j in range(len(local_48)):
  local_c = 0
  while True:
    iVar1 = countChar(s)
    if local_c >= iVar1:
      break
    local_14 = int(ord(s[local_c]))
    # print(iVar1, local_14)
    # print(local_14+local_10)
    if (local_14+local_10) == local_48[j]:
      flag += s[local_c]
    local_c += 1

print(len(local_48))
print(flag)