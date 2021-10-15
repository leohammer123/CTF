from pwn import *
import json

json_data = json.dumps({'buy': 'flag'})
HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(host=HOST,port=PORT)
r.sendlineafter(b'ok',json_data.encode())
r.interactive()