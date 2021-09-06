import hashlib
from io import StringIO
cipher = b'\x1d\x80\x1d\xe0\xa7\x89\x9d\x0f3\xa03`z\x8d\x1b\xbc\xe4\xb7\xcec9\x7f\x8d\x00\xbf\xee\xb7\xc0>js\xafa'
plain_text = []
for key in range(256): # brute-force every possible key
    String = ''
    for r in cipher:
        String += chr(r^key)
        key = hashlib.md5(bytes([key])).digest()[0]
        if key == 0:
            key += 1
    plain_text.append(String)

for r in plain_text:
    if r.find('ictf')!= -1:
        print(r)