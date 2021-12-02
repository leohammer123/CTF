from os import path
from lupa import LuaRuntime    
import lupa  

lua = LuaRuntime(unpack_returned_tuples=True)    

a = open('log.output','r',encoding='utf-8').read().split('char')
for i in a:
    try:
        num = []# Use to store all index
        char = i.replace('\n','').split(':')[0]
        fc = i.split(':')[1]
        lua_func = lua.eval(fc)# function define can't contain name 
        
        if char==" 5":# For bit32 doesn't work
            
            open('char.txt','a').write(str(char)+" "+"10"+"\n")
            continue
            
            
        for r in range(0,35):
            
            a = lua_func(r)
            
            if(a):
                num.append(r)
                
  
        if len(num)>0:
            open('char.txt','a').write(str(char)+" "+' '.join(str(v) for v in num)+"\n")
            
    except Exception as e:
        #print(char)
        pass