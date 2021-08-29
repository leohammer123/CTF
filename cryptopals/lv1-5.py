plain_text = """Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"""
def xor (plain_text,key):
    cipher = ''
    print(len(plain_text))
    for i in range(len(plain_text)):
        u = i%len(key) 
        cipher += chr(ord(plain_text[i]) ^ ord(key[u]))
    return cipher

key = 'ICE'

cipher = xor(plain_text,key=key)

hex_string = ''
for n in cipher:
    hex_string += str(hex(ord(n)))[2:]

print("0"+hex_string)
