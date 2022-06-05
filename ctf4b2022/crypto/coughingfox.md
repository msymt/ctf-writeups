# CoughingFox: 443 team solved

※もっと簡単に解ける方法があると思います。

## Description

55 pt, beginner

author:ushigai

きつねさんが食べ物を探しているみたいです。

## SOLUTIONS

output.txtにフラグを暗号化したデータが入っていました。
フラグの対象となる文字列に対して1つずつ適用し、一致すればその平文を保存してみると、次の文字列が該当しました。
`['w', 'e', 'e', 'e', 'r', 't', 't', 'y', 'u', 'u', 'u', 'o', 'o', 'o', 'o', 'o', 'o', 'a', 'a', 'a', 'a', 's', 'h', 'x', 'n', 'n', 'n', 'T', 'T', 'Y', 'Y', 'D', 'F', 'H', 'H', 'C', 'C', 'N', ',', ',', '?', '?']`

```python
from operator import ne
from random import shuffle

# len(X): 42
FLAG = b"ctf4b{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"
# flagの正規表現から対象となる文字列を列挙
data = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,!@#$%^&*()_+-=[]{}|;':<>?/~`"
# output.txt
origin_ci = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

# 場所は不一致な平文の保存
seed = []

def solve(flag):
    cipher = []
    origin = []
    for i in range(len(flag)):
        f = flag[i]
        c = (f + i)**2 + i
        cipher.append(c)
        # added
        for j in range(len(origin_ci)):
            if c == origin_ci[j]:
                origin.append(chr(f))
                break
    # ctf4b{} は確定で入るため、7以外だと被っている
    if(len(origin) != 7):
        print(origin[6:-1]) # ctf4{...} -> ...
        seed.extend(origin[6:-1])

if __name__ == "__main__":
    cnt = 0
    for c in data:
        full = c * 42
        # ctf4b{...}の中身だけ、全て同じ
        flag = b"ctf4b{" + full.encode() + b"}"
        solve(flag)
    print(seed)
    print(''.join(seed))
```

該当する文字列は分かったので、次にその位置を特定する必要があります。
そこで、1個ずつ入れていき、当てはまった(`ctf4b{...}`と数が7個以上)時だけ保存しました。

```python
from operator import ne
from random import shuffle

# len: 42
id = b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chal_ori = ['w', 'e', 'e', 'e', 'r', 't', 't', 'y', 'u', 'u', 'u', 'o', 'o', 'o', 'o', 'o', 'o', 'a', 'a', 'a', 'a', 's', 'h', 'x', 'n', 'n', 'n', 'T', 'T', 'Y', 'Y', 'D', 'F', 'H', 'H', 'C', 'C', 'N', ',', ',', '?', '?']
origin_ci = [12147, 20481, 7073, 10408, 26615, 19066, 19363, 10852, 11705, 17445, 3028, 10640, 10623, 13243, 5789, 17436, 12348, 10818, 15891, 2818, 13690, 11671, 6410, 16649, 15905, 22240, 7096, 9801, 6090, 9624, 16660, 18531, 22533, 24381, 14909, 17705, 16389, 21346, 19626, 29977, 23452, 14895, 17452, 17733, 22235, 24687, 15649, 21941, 11472]

def challenge(flag, ch):
    cipher = []
    origin = []
    for i in range(len(flag)):
        f = flag[i]
        c = (f + i)**2 + i
        cipher.append(c)
        # added
        for j in range(len(origin_ci)):
            if c == origin_ci[j]:
                origin.append(chr(f))
                break
    if(len(origin) != 7):
        print(ch.decode('utf-8'), end="")
        return True
    return False


for i in range(len(id)):
  for c in chal_ori:
    prefix = id[:i]
    suffix = id[i+1:]
    # ctf4b{XXX... c ...XXX}
    flag = b"ctf4b{" + prefix + c.encode() + suffix + b"}"
    result = challenge(flag, c.encode())
    if(result):
      break
print("")
```

```bash
python3 solve.py
Hey,Fox?YouCanNotTearThatHouseDown,CanYou?
```

## FLAG

```
ctf4b{Hey,Fox?YouCanNotTearThatHouseDown,CanYou?}
```

