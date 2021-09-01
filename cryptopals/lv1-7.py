import base64

def distance (str1,str2):
    assert type(str1)!=type(str2)
    distance = 0
    for i in range(len(str1)):
        binary_xor = ord(str1[i])^ord(str2[i])
        for n in bin(binary_xor)[2:]:
            if n == str(1):
                distance += 1
    return distance

with open('cryptopals\\6.txt','r') as i:
    n  = i.read().split('\n')
    r = []
    for u in n:
            r.append(base64.b64decode(u.replace('\n','')))
    