# Not an RSA challenge
## Entrypoint : Iterator all possibility
### Random part
It seems that it use the os.urandom() function to generate random key , and it is definitely very "random" , but it take an argument 1 , this meant it only generate a byte , which is eazy to iterate.
### Pattern 
```python
for m in flag:
  c.append(a ^ m)
  a = (a + b) % 256
```
In this part of code , it show how the next encrypt key was generated according to a and b value. 
### Solve.py