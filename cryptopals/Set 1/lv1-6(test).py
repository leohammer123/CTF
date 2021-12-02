import base64
import requests

def ascii():
  """Generate ASCII characters."""
  return [chr(x) for x in range(128)]

def remote():
  """Retrieve ciphertext from the Cryptopals site."""
  url = "https://cryptopals.com/static/challenge-data/6.txt"
  return requests.get(url).text

def xor_matching(a:bytes, b:bytes)->list:
  """XOR two sets of bytes with matching lengths."""
  assert len(a) == len(b), 'attempting to XOR with elements of different lengths'
  return [a[i] ^ b[i] for i, x in enumerate(a)]

def hamming_distance(a:bytes, b:bytes)->int:
  """Compute the Hamming distance between two inputs."""
  xor_bytes = xor_matching(a, b)
  binary_bytes = [bin(i)[2:] for i in xor_bytes]
  binary_string = ''.join(binary_bytes)
  binary = list(map(int, list(binary_string)))
  count = sum(binary)
  return count

def key_sizes():
  """Generate a list of possible key sizes."""
  start = 2
  end = 40
  return list(range(start, end + 1))

def split_chunks(iterable,size):
    chunks = [iterable[i:i+size] for i in range(0,len(iterable),size) if i<len(iterable)-size]
    return chunks

def normalized_hamming_distance(text,size):
    bytelist = base64.b64decode(text)
    chunks = split_chunks(bytelist,size)
    blocks = [bytelist[0:size],bytelist[size:size*2]]
    dis = [[hamming_distance(block,chunk)for chunk in chunks] for block in blocks][0]
    mean = sum(dis)/len(dis)
    normal_score = mean/size
    return normal_score

def smallest(values):
  """Find the key sizes corresponding to the smallest Hamming distances in a list."""
  sorted_values = sorted(values, key=lambda x: x.get('distance'))
  return sorted_values[0].get('key_size')

def find_key_size(text):
  """Find the most likely key size for a piece of encrypted text."""
  # compute hamming distance
  normalized_hamming_distances = [
    {
      'key_size': key_size,
      'distance': normalized_hamming_distance(text, key_size)
    } 
    for key_size
    in key_sizes()
  ]
  # choose the smallest key size
  keys = smallest(normalized_hamming_distances)
  return keys

def transpose(text, size):
  """Transpose input text bytes by a specified size."""
  bytelist =base64.b64decode(text)
  chunks = split_chunks(bytelist, size)
  transposed = list(zip(*chunks))
  # check that transposition worked as expected
  assert chunks[0][0] == transposed[0][0], 'matrix transposition failed'
  assert chunks[0][1] == transposed[1][0], 'matrix transposition failed'
  assert chunks[0][2] == transposed[2][0], 'matrix transposition failed'
  return transposed

def xor_single(bytelist, key):
  """XOR a set of bytes against a single key."""
  return [b ^ key for b in bytelist]

def detect_key(strings):
  """Guess a likely key given a set of inputs."""
  common = list('etaoin shrdlu')
  counts = [
    sum([string.count(character) for character in common])
    for string in strings
  ]
  maximum = max(counts)
  index = counts.index(maximum)
  return chr(index)

def find_xor_key(bytelist):
  """For a set of XOR encrypted input bytes, statistically determine the single most likely key."""
  xor_bytes = [xor_single(bytelist, ord(character)) for character in ascii()]
  xor_strings = [''.join(list(map(chr, integer))) for integer in xor_bytes]
  key = detect_key(xor_strings)
  return key

def find_vignere_key(text):
  """Statistically determine the Vignere cipher key that was used to XOR encrypt an input text."""
  key_size = find_key_size(text)
  transposed_bytes = transpose(text, key_size)
  vignere_key = ''.join([find_xor_key(x) for x in transposed_bytes])
  return vignere_key

def decrypt_vignere(ciphertext, key):
  """Given a ciphertext and a key as input, decrypt with a Vignere cipher."""
  bytes_text = base64.b64decode(ciphertext)
  bytes_key = ascii_to_bytes(key)
  decrypted_bytes = [b ^ bytes_key[i % len(bytes_key)] for i, b in enumerate(bytes_text)]
  decrypted_characters = [chr(b) for b in decrypted_bytes]
  decrypted_text = ''.join(decrypted_characters)
  return decrypted_text

def ascii_to_bytes(text):
  """Convert ASCII text to bytes."""
  return bytearray.fromhex(text.encode("utf-8").hex())


def test():
  """Test challenge 6."""
  print('Challenge 6')
  ciphertext = remote()
  key = find_vignere_key(ciphertext)
  assert key == 'Terminator X: Bring the noise', 'incorrect key'
  message = decrypt_vignere(ciphertext, key)
  
  print(key)
  print(message)
  return (key, message)

test()