import codecs
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, base, modes
from cryptography.hazmat.backends import default_backend
import base64
def aes_ecb_decrypt(key, text):
    """
    Decrypts a message encrypted using AES in ECB mode.
    @param key [str]: key
    @param text [str]: CT (hex string)
    @returns [str]: PT (ASCII string)
    """
    cipher = Cipher(algorithms.AES(key), modes.ECB(),
                    backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(text) + decryptor.finalize()

if __name__=='__main__':
    key = 'YELLOW SUBMARINE'
    with open('C:\\Users\\j0704\\OneDrive\\文件\\GitHub\\CTF\\cryptopals\\Set 1\\7.txt', 'r') as f:
        txt = ''.join([line.strip() for line in f])
    hextxt = base64.b64decode(txt)
    print(aes_ecb_decrypt(key.encode(), hextxt))