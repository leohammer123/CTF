import codecs
def xor(text,key):
    xored =''
    for i in text:
        xored += chr(int(i,16)^ord(key))
    return xored
lst = []
plain_text = ''
strings = 'b1 a5 93 a5 e2 a5 f6 a5 c6 a5 b6 a5 11 a5 f3 a5 32 a5'
strings = strings.split(' ')
strings = xor(strings,'\xa5')
for r in strings:
    lst.append((hex(ord(r))[2:])[::-1])

for r in lst:
    plain_text += chr(int(r,16))

print(plain_text.replace('\n',''))