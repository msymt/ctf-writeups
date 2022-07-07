t1 = "c4{fAPu8#FHh2+0cyo8$SWJH3a8X"
t2 = "tfb%s$T9NvFyroLh@89a9yoC3rPy&3b}"

res = ""
t1_idx = 0
t2_idx = 0

for i in range(len(t1) + len(t2)):
  if i % 3 == 0 or i % 5 == 0 :
    res += t1[t1_idx]
    t1_idx += 1
  else:
    res += t2[t2_idx]
    t2_idx += 1

print(res)
