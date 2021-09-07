with open('flag','rb') as n:
    content = n.read()
    r= content.decode().replace('[1A','').replace('\x1b','').replace('\n','')
    pure_string = ''
    for m in r:
        pure_string += m
    print(pure_string[pure_string.find('ictf{'):pure_string.find('ictf{')+63])
        