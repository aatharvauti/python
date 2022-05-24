#!/usr/bin/python
import string

cipher_text = input("Enter Cipher Text to Decrypt: ") 

def decrypt(cipher_text, key): 
    plain_text = ""
    
    cipher_text = cipher_text.lower() 
    for c in cipher_text: 
        if c in string.ascii_letters: 
            tmp = ord(c) + key 
            
            if tmp > ord('z'): 
                tmp = tmp - 26 
    
            plain_text = plain_text + chr(tmp) 
        else: 
            plain_text = plain_text + c
                
    return plain_text

for key in range(26):
    print("Using Key: " + str(key))
    print(decrypt(cipher_text, key))