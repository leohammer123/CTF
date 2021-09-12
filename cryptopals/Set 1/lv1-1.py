hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

import codecs,base64,binascii

a = base64.b64encode(codecs.decode(hex_string,'hex')).decode()
print(a)

g = base64.b64encode(bytearray.fromhex(hex_string)).decode()
print(g)

c = base64.b64encode(binascii.unhexlify(hex_string)).decode()
print(c)