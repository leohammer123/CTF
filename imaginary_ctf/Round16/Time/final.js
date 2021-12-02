if(Date.now() > 12345) {//1640995200000
    var _0x6eaf=["now",
    "\x6c\x69\x7b\x72\x62\x77\x45\x77\x42\x5c\x5b\x45\x1e\x0f\x14\x33\x3a\x2f\x33\x00\x36\x1a\x1a\x15\x18\xdd\xf3\xfe\xf0\xe0\xfe\xcc\xfa\xc8\xce\xd7\xd2\xe1\xa2\xa6\xa9\x8d\xa5\xb9\x8d\x83\x8a\x83\x90\xa5\x8b\x6c\x60\x7d\x4c\x7b\x75\x43\x4b\x40\x6e\x57\x4f\x1f\x2b\x25\x20\x3a\x24"
    ,"","length","random","floor","charCodeAt","fromCharCode","innerHTML","main","getElementById"];
    let b = false; //Date[_0x6eaf[0]]() <= 0x17e12ef9c00;
    let a = _0x6eaf[1];
    let c = _0x6eaf[2];
    for (let i = 0; i < a[_0x6eaf[3]]; i++) {
        let d = b ? Math[_0x6eaf[5]](Math[_0x6eaf[4]]() * 97) + 32 : 5 * (i + 1) % 256;
        c += String[_0x6eaf[7]]((a[_0x6eaf[6]](i) ^ d) % 256)
    };
    //document[_0x6eaf[10]](_0x6eaf[9])[_0x6eaf[8]] = c
    console.log(c)
} else {
    document.getElementById('main').innerHTML = '<h1>Oops...</h1><div>This challenge isn\'t supposed to be released until next year!.</div><br><br>Please try again later.';
}