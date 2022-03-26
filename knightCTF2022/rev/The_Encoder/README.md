# The Encoder

## description

50

A friend of mine sent me the following numbers and the binary and told me that he used that binary to encrypt something interesting for me.

1412 1404 1421 1407 1460 1452 1386 1414 1449 1445 1388 1432 1388 1415 1436 1385 1405 1388 1451 1432 1386 1388 1388 1392 1462

Can you find out what all these numbers mean?

## writeup

Ghidraで開いてみた．

```c
undefined8 main(void){
  int iVar1;
  char local_48 [52];
  uint local_14;
  int local_10;
  int local_c;
  
  local_10 = 0x539;
  local_14 = 0;
  puts("Welcome to the encoder");
  puts("Please give me a plain text of max 40 characters");
  fgets(local_48,0x28,stdin);
  local_c = 0;
  while( true ) {
    iVar1 = countChar(local_48);
    if (iVar1 <= local_c) break;
    local_14 = SEXT14(local_48[local_c]);
    printf("%d ",(ulong)(local_10 + local_14),(ulong)local_14);
    local_c = local_c + 1;
  }
  return 0;
}


int countChar(long param_1){
  int local_10;
  int local_c;
  
  local_c = 0;
  local_10 = 0;
  while (*(char *)(param_1 + local_10) != '\0') {
    if (*(char *)(param_1 + local_10) != '\n') {
      local_c = local_c + 1;
    }
    local_10 = local_10 + 1;
  }
  return local_c;
}
```

FLAGで使われる記号を全て入力して，対応する4桁の数字を配列に格納して，問題文の`1412 1404 1421 1407 1460 1452 1386 1414 1449 1445 1388 1432 1388 1415 1436 1385 1405 1388 1451 1432 1386 1388 1388 1392 1462`に対応する記号を出力すれば良い．

ちなみ`SEXT14`とは

> SEXT14(x) - signed extension The 1 is the size of the operand x The 4 is the size of the output in bytes This is probably a cast from a small signed integer into a big signed integer.
http://wapiflapi.github.io/2019/10/10/efficiency-reverse-engineering-with-ghidra.html

## FLAG

```txt
KCTF{s1Mpl3_3Nc0D3r_1337}
```
