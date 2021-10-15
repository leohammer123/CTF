from pwn import xor
import codecs

cipher = codecs.decode('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104','hex')
len = 0

key = xor(cipher[:7],b'crypto{')
true_key = (key.decode()+'y').encode()#purely guess

print(f'flag : {xor(true_key,cipher).decode()}')



