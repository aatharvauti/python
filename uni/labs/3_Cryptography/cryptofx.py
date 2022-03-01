
def read_file(file):
    f = open(file, 'r')
    plain_text_r = f.read()
    f.close()

    return plain_text_r


def write_file(file, cipher_text_w):
    with open(file, 'w') as f:
        f.write(cipher_text_w)
        f.close()

    return cipher_text_w


def encrypt(file, passwd):

    plain_text = read_file(file)
    cipher_text = ""

    for char in plain_text:
        ascii_val = ord(char)
        encrypted_ascii_val = (ascii_val + passwd) % 128
        encrypted_char = chr(encrypted_ascii_val)

        print(f"\nASCII value of {char} is {ascii_val}\nEncrypted to {encrypted_ascii_val} is {encrypted_char}\n")

        cipher_text = cipher_text + encrypted_char

    write_file(f"{file}_encrypted.txt", cipher_text)

    print(f"Saved the encrypted message to {file}_encrypted.txt")


def decrypt(file, passwd):

    cipher_text = read_file(file)
    plain_text = ""

    for encrypted_char in cipher_text:
        encrypted_ascii_val = ord(encrypted_char)
        ascii_val = (encrypted_ascii_val - passwd) % 128
        char = chr(ascii_val)

        print(f"\nASCII value of {encrypted_char} is {encrypted_ascii_val}\ndecrypted to {ascii_val} is {char}\n")

        plain_text = plain_text + char

    write_file(f"{file}_decrypted.txt", plain_text)

    print(f"Saved the decrypted message to {file}_decrypted.txt")


