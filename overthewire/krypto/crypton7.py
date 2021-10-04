crypt = 'EICTDGYIYZKTHNSIRFXYCPFUEOCKRN'
ciphertext = "PNUKLYLWRQKGKBE"


for i in range(len(ciphertext)):
    k = ord(ciphertext[i]) - ord(crypt[i])
    if k < 0: k += 26
    k += ord('A')
    print(chr(k), end='')
