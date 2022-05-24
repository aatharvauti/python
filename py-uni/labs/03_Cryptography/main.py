
import cryptofx

print("Enter Filename: ")
filename_input = input()

print("Enter Password: ")
passwd_input = int(input())

print("Select an option:\n1. Encryption\n2. Decryption\nChoice: ")
ch = int(input())

if ch == 1:
    cryptofx.encrypt(filename_input, passwd_input)
if ch == 2:
    cryptofx.decrypt(filename_input, passwd_input)

