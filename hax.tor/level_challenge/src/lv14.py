import re
string = ' 9 e 9 2 5 e 9 3 4 1 b 4 9 0 b f d 3 b 4 c 4 c a 3 b 0 c 1 e f 2 0 7 c c 6 9 4 b 9 b 3 f c 6 3 6 7 1 0 f a 0 8 b 6 9 2 2 c 4 2 b e 2 a 7 1 0 6 f 1 c c 8 b b 1 e 1 3 1 8 d f 7 0 a a 0 a 3 5 4 0 c 2 0 a d 4 d 7 6 f e 9 7 7 5 9 a a 2 7 a 0 c 9 9 b f f 6 7 1 0 8 9 7 5 9 e 1 2 8 4 e 2 4 7 9 b 9 9 1 d 2 6 6 9 d e 1 0 4 9 4 2 '
n  = re.findall('.'*32,string.replace(' ',''))
for i in n:
    print(i)