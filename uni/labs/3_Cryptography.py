plain_text = 'Hello World'

# print("Enter Password: ")
# passwd = int(input())
passwd = 1234

cipher_text = []
decrypted_text = []

def encryption():
    for char in plain_text:
        cl = (ord(char) + passwd) % 128
        cipher_text.append(cl)

encryption()

print(f'Encrypted Text: {cipher_text}')

def decryption():
    for y in range(len(cipher_text)):
        pl = (chr(cipher_text[y]) - passwd) % 128
        print(pl)
        # decrypted_text.append(str(pl))
#
decryption()
#
# v = ''
# decrypted_text = v.join(decrypted_text)
#
print(f'Decrypted Text: {decrypted_text}')
