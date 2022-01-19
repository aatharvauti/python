
# calculator

# add -> 2 variables
# always return odd number
# always return values between 0 and 100
# division -> 2 variables
# value of floor division * value of remainder
# a // b * a % b

def add(a, b):
    res = a + b
    if res >= 100:
        res = 99
    elif res <= 0:
        res = 1
    elif res % 2 == 0:
        res = res - 1
    else:
        pass

    return res


def division(c, d):
    res = (c // d) * (c % d)
    return res


print("Menu\n0 for Addition \n1 for Division\n")
ch = input()
print("Enter 2 values")
x = int(input())
y = int(input())

if int(ch) == 1:
    print(division(x, y))
elif int(ch) == 0:
    print(add(x, y))
else:
    pass
