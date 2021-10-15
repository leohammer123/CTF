import base64
import codecs
flag = base64.b64encode(codecs.decode('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf','hex'))
print(flag.decode())