
with open('Round15\Always forward, never back\puzzle.txt','r') as r:
    n = r.read()
    strings = ''
    for k in n.split('\n'):
        strings+=k[0]

    print('ictf{'+strings+'}')
