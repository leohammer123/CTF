from pwn import *
from secrets import randbelow

alphabet = 'abcdefghijkmnopqrstuvwxyz'
payload =''


with open("wordlist.txt") as word_list:
    words = word_list.read().split()
    s = remote('puzzler7.imaginaryctf.org',9000)
    s.recvline_contains(b"RegEx Number 1, or exact guess:")
    payload = alphabet[0]
    for i in range(10):
        s.sendline(payload.encode())
        a = s.recvline_contains(b'No')
        print(a.decode())
        if a.decode().find('No!')!=-1:
            payload = alphabet[i+1]
            print(f'{payload} not work')
        else:
            print(payload)
            break
    r =s.recvline_contains(b'or exact guess: ')
    times = r.decode().split('r')[1]
    times = times.split(',')[0].strip()
    print(times)
    s.send(b'123')
    s.close()