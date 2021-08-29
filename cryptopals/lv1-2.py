import codecs

o = '1c0111001f010100061a024b53535009181c'
k = '686974207468652062756c6c277320657965'
ans = ''
k = codecs.decode(k,'hex')
o = codecs.decode(o,'hex')

def xor (cipher,key):
    plain_text = ''
    for i in range(18):
        plain_text += chr(cipher[i] ^ key[i])
    return plain_text

for i in xor(o,k):
    ans += str(hex(ord(i)))[2:]
print(ans)