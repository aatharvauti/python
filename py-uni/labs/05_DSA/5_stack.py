
print("Atharva Auti Roll No. 1\nStack Data Structure using Python\n")  

stack = [] 

while True:  
    print("""
1. PUSH
2. POP
3. Display
4. Exit
    """)
    ch = int(input("Enter your choice: "))  

    
    if ch == 1:   
        ele = input("Enter Element: ")
        stack.append(ele)
        print("Stack: ", stack)


    elif ch == 2:
        if len(stack) == 0:
            print("The stack is empty!") 
        else:    
            print("\nDeleted: ")  
            print(stack.pop())
            print("Stack: ", stack)

    elif ch == 3:
        if len(stack) == 0:
            print("The stack is empty!") 
        else:
            print("Stack: ", stack)

    elif ch == 4:  
        break  

    else:  
        print("ERR: Invalid Choice!")