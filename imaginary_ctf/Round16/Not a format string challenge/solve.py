with open('imaginary_ctf\\Round16\\Not a format string challenge\\public\\lol','rb') as f:
    r = f.read()
    flag = ''
    location = r.find(b'ictf')# find() can use to find byte.

    for i in range(location,location+22):
        flag += chr(r[i])
    
    print(flag)