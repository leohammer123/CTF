import codecs
from operator import itemgetter



occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

o = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
ans = ''
plaintext_list = []
o = codecs.decode(o,'hex')

def xor (cipher,key):
    plain_text = ''
    for n in range(len(o)):
        plain_text += chr(cipher[n] ^ key)
    return plain_text

def get_score(string):
	score=0
	for char in string:
		char=char.lower()
		if char in occurance_english:
			score+=occurance_english[char]
	return score
    

for i in range(256):
    plaintext_list.append(xor(o,i)) 
sort_o = []
for n in plaintext_list:
    score = get_score(n)
    result={
		'score':score,
		'plaintext':n,
		}
    sort_o.append(result)
newlist = sorted(sort_o, key=itemgetter('score'))[-6]
print(newlist) 


#print(max(plaintext_list, key=lambda s: s.count(' ')))
