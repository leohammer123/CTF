# File Formats
### 1 : Unzip flag.zip
```
unzip flag.zip
```
### 2 : Generate secret.rar's hash
Secret.rar is password-protected so we have to figure out a way to get password . In this case , I use rar2john to generate a hash that could be use to brute force the password by john the ripper.
```
rar2john secret.rar > hash
john --wordlist=/usr/share/wordlist/rockyou.txt hash
```
### 3 : Use the password to encrypt secret.rar file
```
unrar e secret.rar # Enter the password
```
