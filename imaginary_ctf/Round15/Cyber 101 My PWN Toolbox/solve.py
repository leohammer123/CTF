from math import e
from pwn import *
from tqdm import tqdm

amount = 500

r = remote("puzzler7.imaginaryctf.org",2500)

r.recvuntil(b'Ok Go!')
for i in range(amount):
    try:
        dat = r.recv().decode()
        if(dat=='\n'):
            continue
        print(dat)
        ans = eval(dat)
        print(ans)
        r.sendline(str(ans))
    except Exception as e:
        break

