from pikepdf import Pdf

charset= list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_-+=}{[]|:;<>,.?')
passlen = 16

for x in range(1,1000):
    password = ''


    state = x * 48271 % 2147483647
    for i in range(passlen):
        index = state%len(charset)
        nextChar = charset[index]
        password += str(nextChar)
        state = state* 48271 % 2147483647


    try:
        pdf = Pdf.open('invoice.pdf',password=str(password))
        print('correct password: '+str(password))
        exit()
    except Exception as e:
        print('incorrect password :'+str(password))