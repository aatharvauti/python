ques = "label"
flag = ''

for x in ques:
	flag += chr(ord(x) ^ 13)

# converting each character in "label" to integer
# integer xor 13
# interger to character

print(flag)
