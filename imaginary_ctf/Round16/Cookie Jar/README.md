# Cookie jar
# Step 1 : Decompile cookie.jar
### In this case, I use https://github.com/java-decompiler/jd-gui to decompile it, and get something like this.
![https://github.com/leohammer123/CTF/blob/main/imaginary_ctf/Round16/Cookie%20Jar/picture/demo.png]()
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
!()[]
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
## Step 4 : Assemble flag
#### This is the eaziest part , it could even done by hand.
