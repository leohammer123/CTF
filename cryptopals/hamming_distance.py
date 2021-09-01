str1 = 'this is a test'
str2 = 'wokka wokka!!!'

distance = 0
for i in range(len(str1)):
    binary_xor = ord(str1[i])^ord(str2[i])
    for n in bin(binary_xor)[2:]:
        if n == str(1):
            distance += 1
        

print(f'hamming distance is {distance}')

