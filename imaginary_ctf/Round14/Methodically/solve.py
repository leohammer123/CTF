import requests

a = requests.api.request(method='IMAGINARY',url = 'https://method.max49.repl.co/')

print(a.text)