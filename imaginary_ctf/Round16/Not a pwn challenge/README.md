# Not a pwn challenge
## Entrypoint : Break the code into several function.
### In the first begining i try the seed() function.
```python
def rand(seed):
  return eval(bytes([n^(eval(("0b10+"*21)[:-1])) for n in b'CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03\x01CD^\x02IBX\x02\x1e\x13\x03\x03']))
```
### After trying to input different kind of input , we always get the same return value 4. So the jumble() function will always return same value 4*11+4 = 48.
```python
def enc(c: bytes):
  return bytes([_^jumble(rand(42)) for _ in c])
```
### At last the code just encode the flag by xor with 48 , so it can be reverse by xor 48 again due to the feature of xor.

