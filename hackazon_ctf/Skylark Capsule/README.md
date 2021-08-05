# Skylark Capsule
## Tokenz
### First we can regist an account and log in.
![](https://github.com/leohammer123/CTF/blob/main/hackazon_ctf/Skylark%20Capsule/4.png)
### There is a cookie named token,we can try to decode it by [jwt.io](https://jwt.io/).
![](https://github.com/leohammer123/CTF/blob/main/hackazon_ctf/Skylark%20Capsule/1.png)
### You can learn what is jwt at [here](https://jwt.io/introduction),so you can use john the ripper to find the secret key.
![](https://github.com/leohammer123/CTF/blob/main/hackazon_ctf/Skylark%20Capsule/3.png)
### Becauce i already crack it,you can crack it by command
```john --wordlist=/usr/share/wordlists/rockyou.txt new```
### After all, go back to jwt.io enter the secret key and change id = 1,name = admin. Use your new value repalce the previous one 
![](https://github.com/leohammer123/CTF/blob/main/hackazon_ctf/Skylark%20Capsule/2.png)