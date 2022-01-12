import binascii

#string = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
string = binascii.unhexlify("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
print(string)
l = [c for c in string]
for i in range(256):
     f = [chr(n^i) for n in l]
     flag = "".join(f)
     if flag.startswith("crypto"):
             print(flag)
