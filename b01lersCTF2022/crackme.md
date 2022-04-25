# crackme

## description

Security through obscurity is no match for you!

Author: novafacing
Difficulty: Easy

## solution

デコンパイラツールで配布された実行ファイルを開き、main関数を見ると、check関数にて標準入力からの文字列1文字ずつif文で照合してました。

```bash
00401140  uint64_t check(char* arg1)

00401152      int32_t var_c
00401152      if (sx.d(*arg1) != 0x62)
00401158          var_c = 0
0040116f      else if (sx.d(arg1[1]) != 0x63)
00401175          var_c = 0
0040118c      else if (sx.d(arg1[2]) != 0x74)
00401192          var_c = 0
004011a9      else if (sx.d(arg1[3]) != 0x66)
004011af          var_c = 0
004011c6      else if (sx.d(arg1[4]) != 0x7b)
004011cc          var_c = 0
004011e3      else if (sx.d(arg1[5]) != 0x31)
004011e9          var_c = 0
00401200      else if (sx.d(arg1[6]) != 0x33)
00401206          var_c = 0
0040121d      else if (sx.d(arg1[7]) != 0x33)
00401223          var_c = 0
0040123a      else if (sx.d(arg1[8]) != 0x26)
00401240          var_c = 0
00401257      else if (sx.d(arg1[9]) != 0x5f)
0040125d          var_c = 0
00401274      else if (sx.d(arg1[0xa]) != 0x6c)
0040127a          var_c = 0
00401291      else if (sx.d(arg1[0xb]) != 0x65)
00401297          var_c = 0
004012ae      else if (sx.d(arg1[0xc]) != 0x74)
004012b4          var_c = 0
004012cb      else if (sx.d(arg1[0xd]) != 0x6d)
004012d1          var_c = 0
004012e8      else if (sx.d(arg1[0xe]) != 0x65)
004012ee          var_c = 0
00401305      else if (sx.d(arg1[0xf]) != 0x69)
0040130b          var_c = 0
00401322      else if (sx.d(arg1[0x10]) != 0x6e)
00401328          var_c = 0
0040133f      else if (sx.d(arg1[0x11]) != 0x5f)
00401345          var_c = 0
0040135c      else if (sx.d(arg1[0x12]) != 0x31)
00401362          var_c = 0
00401379      else if (sx.d(arg1[0x13]) != 0x32)
0040137f          var_c = 0
00401396      else if (sx.d(arg1[0x14]) != 0x33)
0040139c          var_c = 0
004013b3      else if (sx.d(arg1[0x15]) == 0x7d)
004013c5          var_c = 1
004013b9      else
004013b9          var_c = 0
004013d0      return zx.q(var_c)
```

## FLAG

```
bctf{133&_letmein_123}
```
