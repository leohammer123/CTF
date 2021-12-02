import requests
from lupa import LuaRuntime    

lua = LuaRuntime(unpack_returned_tuples=True)    

url = "https://cookie-jar.ictf.iciaran.com/"
with open('log.output','w',encoding="utf-8") as f:
    for r in range(256):
        if chr(r) in '\n\r': continue
        if not(chr(r).isprintable()) : continue
        cookies = dict(char=chr(r))
        re = requests.get(url,cookies=cookies)
        if re.text.find('<g>')==-1 and re.text.find('Bad')==-1:#Ignore html code
            f.write(f'char {chr(r)}:\n{re.text}')
        try:
            print(f'char {chr(r)} {re.text}')
        except Exception as e:
            print(e)

