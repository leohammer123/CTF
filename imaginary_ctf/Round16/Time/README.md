# Time
### Request directly
Just for testing , I request something like this ``http://puzzler7.imaginaryctf.org:1337/?flag`` , And get the response as we expected.
### Js source 
Althought it looks pretty messy but we can notice that Date.now() function was called and compared with 1640995200000 , this value only show up when we call Date.now() function one year later , so the only way to prevent that is to overwrite source code.
### Edit Js
```javascript
if(Date.now() > 1234) {
    var _0x6eaf = [...];
    let b = Date[_0x6eaf[0]]() <= 0x17e12ef9c00;
    let a = _0x6eaf[1];
    let c = _0x6eaf[2];
    for (let i = 0; i < a[_0x6eaf[3]]; i++) {
        let d = b ? Math[_0x6eaf[5]](Math[_0x6eaf[4]]() * 97) + 32 : 5 * (i + 1) % 256;
        c += String[_0x6eaf[7]]((a[_0x6eaf[6]](i) ^ d) % 256)
    };
    document[_0x6eaf[10]](_0x6eaf[9])[_0x6eaf[8]] = c
} else {
    document.getElementById('main').innerHTML = '<h1>Oops...</h1><div>This challenge isn\'t supposed to be released until next year!.</div><br><br>Please try again later.';
}
```
I thought this will show the flag , but it show some unprintable characters.
### Solution
In this line 
```javascript 
let b = Date[_0x6eaf[0]]() <= 0x17e12ef9c00;
```
Called Date.now() function check if it is bigger or greater than 1640995200000 , and it caused the wrong answer , so all you have to do is to change the code to this.
```javascript 
let b = True;
```