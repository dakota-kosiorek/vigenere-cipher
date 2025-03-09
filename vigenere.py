# Dakota Kosiorek
import re

def encrypt(plain_text: str, key: str):
    regex = re.compile('[^a-zA-Z]')
    plain_text = regex.sub('', plain_text).lower()
    key = regex.sub('', key).lower()
    
    long_key = ''
    long_key = (len(plain_text) // len(key)) * key
    long_key += key[:len(plain_text) - len(long_key)]

    cipher_text = ''

    for p, k in zip(plain_text, long_key):
        cipher_text += chr((( (ord(p) - 97) + (ord(k) - 97) ) % 26) + 65)

    cipher_text = ' '.join(cipher_text[i:i+5] for i in range(0, len(cipher_text), 5))

    return cipher_text

def decrypt(cipher_text: str, key: str):
    regex = re.compile('[^a-zA-Z]')
    key = regex.sub('', key).lower()
    long_key = ''
    long_key = (len(cipher_text) // len(key)) * key
    long_key += key[:len(cipher_text) - len(long_key)]

    decrypted_text = ''
    cipher_text = cipher_text.replace(' ', '').lower()

    for c, k in zip(cipher_text, long_key):
        decrypted_text += chr(((ord(c) - 97) - (ord(k) - 97)) % 26 + 97)

    return decrypted_text

text = 'This is a secret message.'
key = 'code'

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print(encrypted)
print(decrypted)