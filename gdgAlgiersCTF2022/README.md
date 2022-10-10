# GDG Algiers CTF 2022

https://ctftime.org/event/1745

## reverse: traditions

There is a lot of traditions in CTF, and this is the reverse one.

Author : ouxs

### SOLUTION

配布されたバイナリをデコンパイルすると、main関数にて

- フラグ長は0x2f
- フラグの中身は以下のコードで決まる
  ```c
   srand(0x7e6);
   ///
   iVar1 = rand();
   local_20 = (uint)(iVar1 >> 0x1f) >> 0x18;
   local_20 = (iVar1 + local_20 & 0xff) - local_20;
   local_24 = (int)local_118[local_1c] ^ local_20;
   if (local_24 != local_e8[local_1c]) break;
   local_1c = local_1c + 1;
  ```
  - `srand(0x7e6);` によりrand()で呼ばれる値が毎回固定化
  - `local_e8[local_1c]` からフラグを復号するには、`local_e8[local_1c] ^ local_20(randから生成される値)`をすれば良いと判断
    - 入力値がフラグと異なる場合は、`if (local_24 != local_e8[local_1c])`でcmpするときのレジスタの値を変えれば良い。


```c
int main() {
  ///
  srand(0x7e6);
  printf("Enter the password : ");
  fgets(local_118,0x30,stdin);
  sVar2 = strlen(local_118);
  if (sVar2 != 0x2f) {
    printf("Wrong length");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  local_1c = 0;
  while( true ) {
    uVar3 = SEXT48(local_1c);
    sVar2 = strlen(local_118);
    if (sVar2 <= uVar3) {
      puts("Correct, you can submit the flag");
      return 0;
    }
    iVar1 = rand();
    local_20 = (uint)(iVar1 >> 0x1f) >> 0x18;
    local_20 = (iVar1 + local_20 & 0xff) - local_20;
    local_24 = (int)local_118[local_1c] ^ local_20;
    if (local_24 != local_e8[local_1c]) break;
    local_1c = local_1c + 1;
  }
  printf("WRONG");
```

フラグと入力値を比較している様子。

```c
[----------------------------------registers-----------------------------------]
RAX: 0xf0
RBX: 0x24 ('$')
RCX: 0x7f9d3fd5c228 --> 0x2c0f2fff4e56b56
RDX: 0x98
RSI: 0x7ffc0cdc6594 --> 0x9eed41006b4d1d98
RDI: 0x7f9d3fd5c860 --> 0x7f9d3fd5c228 --> 0x2c0f2fff4e56b56
RBP: 0x7ffc0cdc66d0 --> 0x1
RSP: 0x7ffc0cdc65c0 ("CyberErudites{DA_C", 'A' <repeats 28 times>, "}")
RIP: 0x561f2b62a3ed (<main+596>:        cmp    DWORD PTR [rbp-0x1c],eax)
R8 : 0x0
R9 : 0x7f9d3fd5c280 --> 0x8
R10: 0x7f9d3fb4c0f0 --> 0xf0012000027bc
R11: 0x7f9d3fb89760 (<rand>:    endbr64)
R12: 0x7ffc0cdc67e8 --> 0x7ffc0cdc88b3 ("/shared/gdg/prog")
R13: 0x561f2b62a199 (<main>:    push   rbp)
R14: 0x561f2b62cdd8 --> 0x561f2b62a150 (<__do_global_dtors_aux>:        endbr64)
R15: 0x7f9d3fdac040 --> 0x7f9d3fdad2e0 --> 0x561f2b629000 --> 0x10102464c457f
EFLAGS: 0x202 (carry parity adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x561f2b62a3e1 <main+584>:   mov    eax,DWORD PTR [rbp-0x14]
   0x561f2b62a3e4 <main+587>:   cdqe
   0x561f2b62a3e6 <main+589>:   mov    eax,DWORD PTR [rbp+rax*4-0xe0]
=> 0x561f2b62a3ed <main+596>:   cmp    DWORD PTR [rbp-0x1c],eax
   0x561f2b62a3f0 <main+599>:   je     0x561f2b62a410 <main+631>
   0x561f2b62a3f2 <main+601>:   lea    rax,[rip+0xc32]        # 0x561f2b62b02b
   0x561f2b62a3f9 <main+608>:   mov    rdi,rax
   0x561f2b62a3fc <main+611>:   mov    eax,0x0
[------------------------------------stack-------------------------------------]
0000| 0x7ffc0cdc65c0 ("CyberErudites{DA_C", 'A' <repeats 28 times>, "}")
0008| 0x7ffc0cdc65c8 ("dites{DA_C", 'A' <repeats 28 times>, "}")
0016| 0x7ffc0cdc65d0 ("_C", 'A' <repeats 28 times>, "}")
0024| 0x7ffc0cdc65d8 ('A' <repeats 22 times>, "}")
0032| 0x7ffc0cdc65e0 ('A' <repeats 14 times>, "}")
0040| 0x7ffc0cdc65e8 --> 0x7d414141414141 ('AAAAAA}')
0048| 0x7ffc0cdc65f0 --> 0x9100000015
0056| 0x7ffc0cdc65f8 --> 0x590000002a ('*')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 4, 0x0000561f2b62a3ed in main ()
gdb-peda$ x/5b $rbp-0x1c
0x7ffc0cdc66b4: 0xd9    0x00    0x00    0x00    0x98
gdb-peda$ set $rax=0xd9
```

solver

```python
key = [0x42146b34,0x6ee90420,0x5a050610,0x2c640db4,0x618fc5bd,0x2258457d,0x28be5bf2,0x67a79588,0x543d79fd,0x74bd2f62,0x3c90b8ed,0x2210a846,0x136848a4,0x4b9ae47a,0x5e27b305,0x4a35650f,0x36a5fef5,0x2e19bd5b,0x66394ef7,0x2dd6ee3d,0x4c42bb97,0x70c03bf7,0x6b4d1d98,0x46b57142,0x7220b577,0x27c756b,0x5d8dd6da,0xa5c3d5,0x2e09d54a,0x53bba607,0x55561df2,0x701e407e]
data = [0x70,0x61,0x4f,0xf7,0xd1,0x49,0xd6,0xac,0xb4,0x21,0xb2,0x1e,0x94,0x28 ,0x5a,0x57,0xaa,0x15,0xc7,0xa,0xc8,0xa3,0xf0,0x76,0x3,0x34,0x88,0xe1,0x24,0x63,0xc2,0x13]

print("CyberErudites{", end="")
for i in range(len(key)):
    print(chr(data[i] ^ key[i] & 0xff), end="")
print("}")

```

### FLAG

```
CyberErudites{DA_Cl4$$IC_X0R_X_N07_Th4t_R4nd0m}
```

