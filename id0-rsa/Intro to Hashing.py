import hashlib

test_string = b'id0-rsa.pub'

n = hashlib.sha256(test_string).hexdigest()

print(hashlib.md5(n.encode()).hexdigest())

