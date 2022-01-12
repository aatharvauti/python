encrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])
