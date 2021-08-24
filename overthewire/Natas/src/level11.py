import base64
plaintext = '{"showpassword":"no", "bgcolor":"#ffffff"}'
decrypted_cookie=base64.b64decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=").decode()
key = ''

for i in range(0, len(plaintext)):
    j = i % len(decrypted_cookie)
    key += chr(ord(plaintext[i]) ^ ord(decrypted_cookie[j]))
    

print(f'{key}')# key = qw8J

plaintext = '{"showpassword":"yes", "bgcolor":"#ffffff"}'
chipher = ''
key = 'qw8J'


for i in range(0, len(plaintext)):
    j = i % len(key)
    chipher += chr(ord(plaintext[i]) ^ ord(key[j]))

print(base64.b64encode(chipher.encode()).decode())

