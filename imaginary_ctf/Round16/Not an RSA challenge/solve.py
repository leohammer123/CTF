

def xor(var, key) -> bytes:
    return bytes(a ^ b for a, b in zip(var, key))


c = b'\xf2\xa3\x91lT=\r\xed\x9c\x9ahS;\x10\xd8\x99\x85\x7fA\x05\r\xd7\xa8\xb1\x7fW1\xff'
a,b = 0,0

string = []

for r in range(256):
    if (xor(c,bytes([r]))==bytes([ord('i')])):
        a = r

for a in range(256):
    for b in range(256):
        pl = ''
        for r in c:
            pl += chr(r^a)
            a = (a + b) % 256
        string.append(pl)

for r in string:
    if r.startswith('ictf'):
        print(r)
    