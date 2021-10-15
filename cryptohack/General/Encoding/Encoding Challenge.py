from pwn import *
import json
import codecs
import string
import base64
from tqdm import tqdm
from crypto.Util.number import *

def bigint(n):
    return long_to_bytes(int(n,base=16))


def rot13(s):
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     s = s.lower()
     
     keyShift = 13
     strings = ''
     for i in s:
         if i.isalpha():
            encryptedCharacter = alphabet.index(i) + keyShift
            if encryptedCharacter > 25:
                 encryptedCharacter = alphabet.index(i) - keyShift

            strings +=alphabet[encryptedCharacter]
         else:
            strings += i
     return strings.encode()

def bass64(n):
    return base64.b64decode(n)
    
def hex(n):
    return codecs.decode(n,'hex')

def utf8(n):
    fl = list(n)
    strings = ''

    for r in fl:
        strings += chr(r)
    return strings.encode()

host = 'socket.cryptohack.org'
port = 13377


r = remote(host,port)

for j in tqdm(range(100)):

    hex_data = r.recvline()
    hex_data = json.loads(hex_data.decode())
    if str(hex_data).find('err')!=-1:
        print(hex_data)
        exit(0)

    if str(hex_data).find('utf')!=-1:
        hex_data["type"] = "utf8"
    if str(hex_data).find('base64')!=-1:
        hex_data["type"] = "bass64"

    func = hex_data["type"]
    cipher = hex_data["encoded"]

    ret = eval(func)(cipher)
    send_data = json.dumps({"decoded": ret.decode()})
    r.sendline(send_data.encode())


r.interactive()
exit(0)
