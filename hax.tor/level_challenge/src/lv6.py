import codecs

def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes

a= 'b1a593a5e2a5f6a5c6a5b6a511a5f3a532a5'
a = codecs.decode(a,'hex')
print(a)
n = single_char_xor(a,int('5A',base=16)).decode('utf-8')
print(n)