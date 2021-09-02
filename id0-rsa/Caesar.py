def decrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
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


cipher = 'ZNKIGKYGXIOVNKXOYGXKGRREURJIOVNKXCNOINOYXKGRRECKGQOSTUZYAXKNUCURJHKIGAYKOSZUURGFEZURUUQGZZNKCOQOVGMKGZZNKSUSKTZHAZOLOMAXKOZYMUZZUHKGZRKGYZROQKLOLZEEKGXYURJUXCNGZKBKXBGPJADLIVBAYKZNUYKRGYZZKTINGXGIZKXYGYZNKYURAZOUT'

score_list = []
for i in range(27):
        n = decrypt(cipher,i)
        score = get_english_score(n.encode())
        data ={
            'plain_text':n,
            'score':score,
            'shift':i
        }
        score_list.append(data)
print(sorted(score_list, key=lambda x: x['score'], reverse=True)[0])
