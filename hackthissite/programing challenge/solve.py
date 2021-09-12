def count_character(word):
    all_freq = {}
    for i in word:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    all_freq['word']  = word
    return all_freq

def wordlist_freq():
    world_list = []
    with open('wordlist.txt','r')as n:
        r = n.read()
        for i in r.split('\n'):
            world_list.append(count_character(i))
    return world_list

def input_freq():
    input_list = []
    for i in range(10):
        i = input()
        input_list.append(count_character(i))
    return input_list

n = input_freq()
r = wordlist_freq()
for i in n:
    p = 0
    for input_property in i:
        for g in r:
            for wordlist_property in g:
                try:
                    if i[input_property] == g[wordlist_property]:
                        p+=1
                except Exception as e:
                    pass
    if p == len(i):
        print(i)
    