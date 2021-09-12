import base64

def hamming_distance (str1,str2):
    distance = 0
    for i in range(len(str1)):
        binary_xor = ord(str1[i])^ord(str2[i])
        for n in bin(binary_xor)[2:]:
            if n == str(1):
                distance += 1
    return distance

def cal(ciphertext):
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


def get_english_score(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }   
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

def xor (plain_text,key):
    cipher = ''
    print(len(plain_text))
    for i in range(len(plain_text)):
        u = i%len(key) 
        cipher += chr(ord(plain_text[i]) ^ ord(key[u]))
    return cipher

def bruteforce_single_char_xor(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = xor(ciphertext.decode(), chr(key_value))
        score = get_english_score(message.encode())
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]




with open('6.txt','r') as i:
    n  = i.read().split('\n')
    r = ''
    for u in n:
            r += (base64.b64decode(u.replace('\n',''))).decode()
    possible_length = []
    n = 0
    for g in cal(r):
        try:
            possible_length.append(g['key'])
        except Exception as e:
            break
    key = b''
    r = r.encode()
    possible_plaintext = []
    for j in possible_length:
        block = b''
        for j in range(j, len(r), j):
            block += bytes([r[j]])
        key += bytes([bruteforce_single_char_xor(block)['key']]) 
        print(key)
        possible_plaintext.append((xor(r.decode(), key.decode()), key.decode())) 
        print(max(possible_plaintext, key=lambda x: get_english_score(x[0].encode())))


















