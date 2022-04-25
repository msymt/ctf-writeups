# crackme_2 

## description

Time for some basic algebra...

Author: novafacing
Difficulty: Easy

## solution

デコンパイラツールで配布された実行ファイルを開き、main関数を見ると、check関数にて標準入力からの文字列1文字ずつif文で照合してました。
crackmeより、若干複雑度が増している程度でした。

```C
000011a9  uint64_t check(char* arg1)
000011a9  {
000011c3      uint64_t rax_14;
000011c3      if (*(int8_t*)arg1 != 0x62)
000011c1      {
00001215      label_1215:
00001215          rax_14 = 0;
00001215      }
000011d7      else
000011d7      {
000011d7          if (arg1[1] != 0x63)
000011d5          {
000011d7              goto label_1215;
000011d7          }
000011eb          if (arg1[2] != 0x74)
000011e9          {
000011eb              goto label_1215;
000011eb          }
000011ff          if (arg1[3] != 0x66)
000011fd          {
000011ff              goto label_1215;
000011ff          }
00001213          if (arg1[4] != 0x7b)
00001211          {
00001213              goto label_1215;
00001213          }
0000123a          if (0x34 != ((int32_t)arg1[5]))
0000122e          {
0000123c              rax_14 = 0;
0000123c          }
00001264          else if (((int32_t)(arg1[6] ^ 0x33)) != 0x5f)
00001262          {
00001266              rax_14 = 0;
00001266          }
00001282          else if (0x67 != arg1[7])
00001279          {
00001284              rax_14 = 0;
00001284          }
0000129b          else if (arg1[8] != 0x33)
00001299          {
0000129d              rax_14 = 0;
0000129d          }
000012be          else if ((arg1[9] ^ 0x10) != 0x72)
000012bc          {
000012c0              rax_14 = 0;
000012c0          }
000012e9          else if ((arg1[0xa] ^ arg1[9]) != 0x10)
000012e7          {
000012eb              rax_14 = 0;
000012eb          }
00001313          else if ((((int32_t)arg1[0xb]) - 1) != (0x33)
00001307          {
00001315              rax_14 = 0;
00001315          }
00001329          else if (arg1[0xc] != 0x21)
00001327          {
0000132b              rax_14 = 0;
0000132b          }
0000133a          else
0000133a          {
0000133a              rax_14 = ((uint64_t)arg1[0xd]);
00001344              if (rax_14 != 0x7d)
00001342              {
00001346                  rax_14 = 0;
00001346              }
00001342          }
00001342      }
0000134e      return rax_14;
0000134e  }
```

arg[6]あたりからは以下のように総当たりで解きました。

```python
for i in range(0, 255):
  num = xor(i, 98) # 第2は適宜入れ替える
  print(i, hex(num))
```

照らし合わせると以下のような16進数が現れたのでデコードします。
```python
data = [0x62,0x63,0x66,0x7b,0x34,0x6c,0x67,0x33,0x62,0x72,0x34,0x21,0x7d]

for i in data:
  print(chr(i), end="")
```

## FLAG

```
bcf{4lg3br4!}
```
