# 1 Append
# 2 Insert
# 3 Remove
# 4 Pop
# 5 Clear
# 6 Sort
# 7 Reverse
# 8 Length

list=[]
def pl():
    print(list)

while True:
    
    print("""
    Main Menu:
    1: Append
    2: Insert
    3: Remove
    4: Pop
    5: Clear
    6: Sort
    7: Reverse
    8: Length
    """)


    ch = int(input())
    if ch == 1:
        print("Enter the value to append: ")
        appd = input()
        list.append(appd)
        pl()
    elif ch == 2:
        print("Enter the value to insert: ")
        inst = input()
        print("Enter the postion to insert value at: ")
        pos = int(input())
        list.insert(pos, inst)
        pl()
    elif ch == 3:
        print("Enter the value to remove: ")
        remv = input()
        list.remove(remv)
        pl()
    elif ch == 4:
        print("Enter the index to be popped: ")
        popd = int(input())
        list.pop(popd)
        pl()
    elif ch == 5:
        list.clear()
        pl()
    elif ch == 6:
        list.sort()
        pl()
    elif ch == 7:
        list.reverse()
        pl()
    elif ch == 8:
        print(len(list))
        pl()
    else:
        print("Invalid Input: Exiting the Program")



