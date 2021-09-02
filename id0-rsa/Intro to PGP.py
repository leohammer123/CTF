import subprocess


def check(password):
    cmd = 'cat enc.pgp |'
    cmd += f"gpg -d --passphrase {password}"
    cmd += " 2>/dev/null"
    subprocess.run(cmd,shell=True)

filename = "enc.pgp"
f = open(filename, "r")
filedata = f.read()
f.close()
for word in open("/usr/share/wordlists/rockyou.txt", "r"):
    check(word)
