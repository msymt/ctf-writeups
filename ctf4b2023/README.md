# SECCON Beginners CTF 2023 <!-- omit in toc -->

この1年あまりCTFをやってなかったので微妙です。

https://score.beginners.seccon.jp/

- [rev/Half](#revhalf)
- [rev/Three](#revthree)
- [web/Forbidden](#webforbidden)
- [CoughingFox2](#coughingfox2)


## rev/Half

バイナリファイルってなんのファイルなのか調べてみよう！

あとこのファイルってどうやって中身を見るんだろう...？

### SOLUTION <!-- omit in toc -->

stringsでフラグが見れました。

### FLAG <!-- omit in toc -->

```
ctf4b{ge4_t0_kn0w_the_bin4ry_fi1e_with_s4ring3}
```


## rev/Three

このファイル、中身をちょっと見ただけではフラグは分からないみたい！

バイナリファイルを解析する、専門のツールとか必要かな？


### SOLUTION <!-- omit in toc -->

標準入力から受け取った文字列がフラグと一致しているか確認する関数がありました。

```c
// ida freeを使用
__int64 __fastcall validate_flag(const char *a1)　{
  int v2; // eax
  int i; // [rsp+1Ch] [rbp-4h]

  if ( strlen(a1) == 49 ){
    for ( i = 0; i <= 48; ++i ){
      if ( i % 3 ){
        if ( i % 3 == 1 )
          v2 = flag_1[i / 3];
        else
          v2 = flag_2[i / 3];
      }else{
        v2 = flag_0[i / 3];
      }
      if ( (_BYTE)v2 != a1[i] )
        goto LABEL_2;
    }
    puts("Correct!");
    return 0LL;
  }else{
LABEL_2:
    puts("Invalid FLAG");
    return 1LL;
  }
}
```

flag_0からflag_2の中身は以下の通りとなっていました。validate_flagの通り、先頭からそれぞれ1文字ずつ取るとフラグになりました。

```python
# c4c_ub__dt_r_1_4}
flag_0 = [0x63, 0x34, 0x63, 0x5F, 0x75, 0x62, 0x5F, 0x5F, 0x64, 0x74, 0x5F, 0x72, 0x5F, 0x31, 0x5F, 0x34, 0x7D]
# tb4y_1tu04tesifg
flag_1 = [0x74, 0x62, 0x34, 0x79, 0x5F, 0x31, 0x74, 0x75, 0x30, 0x34, 0x74, 0x65, 0x73, 0x69, 0x66, 0x67]
# f{n0ae0n_e4ept13
flag_2 = [0x66, 0x7B, 0x6E, 0x30, 0x61, 0x65, 0x30, 0x6E, 0x5F, 0x65, 0x34, 0x65, 0x70, 0x74, 0x31, 0x33]
```

### FLAG <!-- omit in toc -->

```
ctf4b{c4n_y0u_ab1e_t0_und0_t4e_t4ree_sp1it_f14g3}
```

### REF <!-- omit in toc -->


## web/Forbidden

You don't have permission to access /flag on this server.

### SOLUTION <!-- omit in toc -->

/flagにアクセスしてもフラグは得られません。case sensitivity系かなと思い、大文字に変えるとフラグゲットでした。

```bash
$ curl https://forbidden.beginners.seccon.games/FLAG
ctf4b{403_forbidden_403_forbidden_403}%
```

### FLAG <!-- omit in toc -->

```
ctf4b{403_forbidden_403_forbidden_403}
```

## CoughingFox2

暗号問題に初めて挑戦する方向けに独自暗号と暗号化した後の出力を配布します。 ご覧の通り、簡易な暗号方式なので解読は簡単です。 解読をお願いします！

### SOLUTION <!-- omit in toc -->

配布されたファイルは以下二つです。

```python
# coding: utf-8
import random
import os

flag = b"ctf4b{xxx___censored___xxx}"

# Please remove here if you wanna test this code in your environment :)
flag = os.getenv("FLAG").encode()

cipher = []

for i in range(len(flag)-1):
    c = ((flag[i] + flag[i+1]) ** 2 + i)
    print(c, f, g, (f + g) ** 2)
    cipher.append(c)

random.shuffle(cipher)

print(f"cipher = {cipher}")
```

```txt
cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]
```

昨年の問題と同じく、c - iが平方数になれば良いと考え全探索を試みました。
しかし、任意のiに対して、flag[i]とflag[i+1]の合計が`c - i`と一致するパターンが複数あることに気づきました。
そこで、平文が`ctf4b{...}`とわかっているので、flag[0]=c, flag[1]=t, flag[2]=fと続くパターンを抽出すれば良いと判断しました。

```
# i , flag[i], flag[i+1]
...
0 , c , t
...
1 , t , f
...
2 , f , 4
...
```

以下がそのソルバーです。実行すればフラグが出てきました。

```python
cipher = [4396, 22819, 47998, 47995, 40007, 9235, 21625, 25006, 4397, 51534, 46680, 44129, 38055, 18513, 24368, 38451, 46240, 20758, 37257, 40830, 25293, 38845, 22503, 44535, 22210, 39632, 38046, 43687, 48413, 47525, 23718, 51567, 23115, 42461, 26272, 28933, 23726, 48845, 21924, 46225, 20488, 27579, 21636]
flag = [''] * len(cipher)

data = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,!@#$%^&*()_+-=[]{}|;':<>?/~`"

for i in range(len(cipher)-1):
  for c in cipher:
    for s in data:
      for t in data:
        if c == ((s + t)**2 + i):
          if i == 0:　# チェック用
            if chr(s) == "c" and chr(t) == "t":
              flag[i] = chr(s)
              flag[i+1] = chr(t)
              break
          else:
            if chr(s) == flag[i]:
              flag[i+1] = chr(t)
            break

print("".join(flag))

```

### FLAG <!-- omit in toc -->

```bash
ctf4b{hi_b3g1nner!g00d_1uck_4nd_h4ve_fun!!!}
```
