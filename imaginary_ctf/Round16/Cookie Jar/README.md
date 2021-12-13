# Cookie jar
# Step 1 : Decompile cookie.jar
### In this case, I use https://github.com/java-decompiler/jd-gui to decompile it, and get something like this.
![image](https://github.com/leohammer123/CTF/blob/main/imaginary_ctf/Round16/Cookie%20Jar/picture/demo.png)
## Cookies.class have the check_flag function
```java
  public boolean checkFlag(String flag) {
    boolean valid = true;
    for (int i = 0; i < flag.length(); i++) {
      if (!check(flag.charAt(i), i))
        valid = false; 
    } 
    return valid;
  }
```
## It call another function check
```java

  public boolean check(char c, int i) {
    URL url;
    HttpURLConnection connection;
    try {
      url = new URL("https://cookie-jar.ictf.iciaran.com/");
    } catch (MalformedURLException e) {
      return false;
    } 
    try {
      connection = (HttpURLConnection)url.openConnection();
    } catch (IOException e) {
      return false;
    } 
    connection.setRequestProperty("Cookie", String.format("char=%s", new Object[] { Character.valueOf(c) }));
    try {
      Globals globals = JsePlatform.standardGlobals();
      InputStream responseStream = connection.getInputStream();
      globals.load(new InputStreamReader(responseStream, StandardCharsets.UTF_8), "main.lua").call();
      LuaValue lv = globals.get("check").call((LuaValue)LuaValue.valueOf(i));
      return lv.toboolean();
    } catch (IOException e) {
      return false;
    } 
  }
  
```
#### check function take in two arguments first one is the input character , the second one is the character index. It make a http request to the server with the character using cookie. After that it recive response.<\br>
#### The response is some kind of lua code , and it would be use by luaj , luaj is a java package can run lua. Recive the return boolean value.
# Step 2 : Get lua code
### It return different function while I was trying some different input. So I write a python script to try every possible character.
```python
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
````
## The result show some ofthe interesting thing.
# case `
```lua
function (index)
    return false;
```
### This one is pretty obvious , whether the index value is , it always return flase also means that flag doesn't contain this character.
# case _
```lua
function (index)
    l = {}
    a = 1 
    for n=1, 10 do
        l[n] = a
        a = n*n - a
    end
    for n=6, 8 do
        if l[n] == index then
            return true
        end
    end
    return false
end
```
#### As you can see , the code become hard to read , it take lot of time to do it by hand.
# Step 3 : Get index value
#### Python have a almost same package lupa to run lua , use a loop to iterate all possible index which is 0-35 , if it return true then the flag at that index is that character.
```python
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
 ```
     
## Step 4 : Assemble flag
#### This is the eaziest part , it could even done by hand.
```python
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
```
