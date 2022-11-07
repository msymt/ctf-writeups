# BuckeyeCTF 2022

https://ctftime.org/event/1740

- [[rev beginner] Sinep (274 solves)](#rev-beginner-sinep-274-solves)
- [[rev beginner] soda (178 solves)](#rev-beginner-soda-178-solves): unsolved

## [rev beginner] Sinep (274 solves)

Sinep industries is advertising a Certified unbreakable encryption algorithm. Seeing as it's proprietary and Certified, I'm confident my data is safe. I'm so confident I'll straight up give you the flag.... ENCRYPTED hahahaha 0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e

### SOLUTION

Ghidraでデコンパイルすると、暗号化部分が以下のようになってました。

```c
    local_2e = 0x656e6973;
    local_2a = 0x70;
    input = *(char **)(param_2 + 8);
    printf("Final: 0x");
    cnt = 0;
    while( true ) {
      uVar3 = SEXT48(cnt);
      sVar2 = strlen(input);
      if (sVar2 <= uVar3) break;
      input[cnt] = *(byte *)((long)&local_2e + (long)(cnt % 5)) ^ input[cnt];
      printf("%02x");
      cnt = cnt + 1;
    }
    putchar(10);
    uVar1 = 0;
  }
```

問題文から、暗号化によって`0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e`が生成されれば良いと考え、総当たりをしました。

```python
import string

flag_candidates = string.printable
ans = "0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e"
ans = ans[2:]
flag_list = []
for i in range(0, len(ans), 2):
    flag_list.append(ans[i:i+2])
print(len(flag_list), flag_list)

flag = 'buckeye{'
initial_flag_len = len(flag)
flag = list(flag)
sinep = "sinep"

while len(flag) < len(flag_list):
  for c in flag_candidates:
    flag_is_match = False
    flag_for_concat = flag + [c]
    flag_tmp = flag + [c]
    # print(flag_tmp)
    cnt = 0
    while True:
      if cnt >= len(flag_tmp):
        break
      index = cnt
      char_input = (ord(sinep[cnt % 5])) ^ ord(flag_tmp[cnt])
      flag_tmp[index] = chr(char_input)
      cnt += 1
    for i,j in enumerate(flag_tmp):
      res = '{:02x}'.format(ord(j))
      if flag_list[i] == res and i == len(flag_tmp) - 1:
        flag_is_match = True
        break
    if flag_is_match:
      print("match!")
      flag = flag_for_concat
      break

print("".join(flag))
```

```
buckeye{r3v_i5_my_p45510n}
```

---

解けなかった問題

## [rev beginner] soda (178 solves)

Man, I'm parched. I sure hope this vending machine doesn't suck...

`nc pwn.chall.pwnoh.io 13375`

### SOLUTION

`soda.java`から、`wait i>10 ->purchase->tap->reach->grab `の順番で実行すればよいと考えたが、Fail。

```bash
command> grab
>> Alright!! Let's see what I got!
>> No flags in here... was the prophecy a lie...?

-------------------------------------------
| 1    | 2    | 3    | 4    | 5    | 6    |
|      |      |  __  |  __  |      |      |
|      |      | |  | | |  | |      |      |
|      |      | |__| | |__| |      |      |
|      |      |      |      |      |      |
| 3.44 | 0.34 | 3.77 | 5.48 | 4.01 | 0.29 |
-------------------------------------------
| 7    | 8    | 9    | 10   | 11   | 12   |
|      |  __  |      |      |  __  |  __  |
|      | |  | |      |      | |  | | |  | |
|      | |__| |      |      | |__| | |__| |
|      |      |      |      |      |      |
| 5.93 | 3.46 | 2.92 | 3.28 | 3.49 | 3.18 |
-------------------------------------------

I have $1.74 in my wallet
```

```java
// soda.java
// grab()->retrieve()で、残った商品のコストが最も高く、かつそのSTATUSがDROPPEDのときフラグが出力される
    public void retrieve() {
      byte b = -1;
      float f = -1.0F;
      for (byte b1 = 0; b1 < 12; b1++) {
        if ((this.drinks[b1]).status != soda.Drink.DrinkStatus.EMPTY && 
          (this.drinks[b1]).cost > f) {
          b = b1;
          f = (this.drinks[b1]).cost;
        } 
      }
      System.out.println(b);
      if ((this.drinks[b]).status == soda.Drink.DrinkStatus.DROPPED) {
        soda.printFlag();
      } else {
        System.out.println(">> No flags in here... was the prophecy a lie...?");
      } 
    }
```


全部の賭け金の合計が$5.00になれば良いと思い回し続けたのですが、$15-$50しか出ませんでした。

```python
from pwn import *

HOST='pwn.chall.pwnoh.io'
PORT=13375
wallet = 5.0

while True:
  conn = remote(HOST, PORT)
  res = conn.recvuntil("command> ")
  res_list = res.decode("utf-8").split("\n")
  first = res_list[9].split(" ")
  second = res_list[16].split(" ")
  first_num = []
  second_num = []

  # first = ['|', '5.26', '|', '5.12', '|', '1.69', '|', '0.58', '|', '5.40', '|', '4.72', '|']

  for i in range(len(first)):
    if i % 2 == 1:
      first_num.append(float(first[i]))

  for i in range(len(second)):
    if i % 2 == 1:
      second_num.append(float(second[i]))

  print(first_num)
  print(second_num)
  sum_v = 0.0
  for i in first_num:
    sum_v += i
  for i in second_num:
    sum_v += i

  print(sum_v)
  if sum_v <= wallet:
    break
  conn.close()

conn.interactive()
```
