from itertools import cycle


def xor(data, key):
    return ''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(data, cycle(key)))

with open('test.bin', 'rb') as encrypted, open('sitecom.bin', 'wb') as decrypted:
    decrypted.write(xor(encrypted.read(), '8A8A8A8A8A8A8A8A'))
