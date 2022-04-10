
# Continuously take input from the user
# and sum the value

# 1) if user has entered multiple of 3, we do not add it to sum
# 2) if sum exceeds 100, stop and print the value

res = 0

while res <= 100:
    a = int(input())
    if a % 3 == 0:
        continue
    res += a

print(res)
