import base64

def hamming_distance (str1,str2):
    distance = 0
    for i in range(len(str1)):
        binary_xor = ord(str1[i])^ord(str2[i])
        for n in bin(binary_xor)[2:]:
            if n == str(1):
                distance += 1
    return distance

def hamming_score(ciphertext):
    average_distances = []

    for key_size in range(2,41):
        chunk = []
        score = []
        for r in range(0,len(ciphertext),key_size):
            chunk.append(ciphertext[r:r+key_size])
        while True:
            try:
                chunk0 = chunk[0]
                chunk1 = chunk[1]
                distance_score = hamming_distance(str1=chunk0,str2=chunk1)/key_size
                score.append(distance_score)
                del chunk[0]
                del chunk[1]
            except Exception as e:
                break
        if len(score)==0:
            continue
        result = {
            'key': key_size,
            'avg distance': sum(score) / len(score)
            }
        average_distances.append(result)
    return  sorted(average_distances, key=lambda x: x['avg distance'])[:5]

def xor (plain_text,key):
    cipher = ''
    print(len(plain_text))
    for i in range(len(plain_text)):
        u = i%len(key) 
        cipher += chr(ord(plain_text[i]) ^ ord(key[u]))
    return cipher


def input_string():
    with open('6.txt','r') as i:
        n = i.read()
    return base64.b64decode(n.replace('\n','')).decode()

def main():
    cipher = input_string()
    



#def len_brute(length):
    #for i in range(length):
        