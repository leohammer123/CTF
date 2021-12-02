flag =[None]*35
index =0 
text = open('Cookie Jar\\answer\char.txt','r').read().split('\n')
flag[33] = "6"



for i in text:
    
    char = i.split(' ')[1]
    dex = i.split(' ')[2:]
    
    for n in dex:

        flag[int(n)] = char
        
        
print("".join(str(c) for c in flag))    


# flag ictf{r3ver51n9_w17h0u7_full_s0urc6}