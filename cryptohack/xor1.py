from pwn import * 
from binascii import unhexlify

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
K2S = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
K3S = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
K4S = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

print("Key1: " + KEY1.hex())

KEY2 = xor(KEY1,K2S)
print("Key2: " + KEY2.hex())

KEY3 = xor(KEY2,K3S)
print("Key3: " + KEY3.hex())

KEY4 = xor(KEY1,KEY2,KEY3)
print("Key4: " + KEY4.hex())

FLAG = xor(K4S,KEY4)
print(unhexlify(FLAG.hex()))