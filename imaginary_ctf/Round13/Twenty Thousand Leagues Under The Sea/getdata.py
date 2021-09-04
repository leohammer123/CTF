from pwn import *
s = remote('puzzler7.imaginaryctf.org',9000)
with open("wordlist.txt",'a',encoding = 'utf-8') as f:
        for i  in range(19):
            atr = f'RegEx Number {i+1}, or exact guess:'
            print(atr)
            p = s.recvline_contains(atr.encode())
            s.sendline(b'123')
    
        a = s.recvline_contains(b'Final guess! What is the word?')
        s.sendline(b'123')
        g = s.recvline_startswith(b'You lose')
        print(g.decode())
        r = g.decode().split(':')[1]
        r = r.split('\\')[0].strip()+"\n"
        f.write(r)
