
print("Atharva Auti Roll No. 1\nLinkedList Data Structure using Python\n")  

import collections

linked_list = collections.deque()

while True:  
    print("""
1. Insert
2. Insert at index
3. Display
4. Delete last element
5. Delete at index
6. Exit
    """)
    ch = int(input("Enter your choice: "))  

    
    if ch == 1:   
        ele = input("Enter element: ")
        linked_list.append(ele)
        print("List: ", linked_list)

    elif ch == 2:
        pos = int(input("Enter position: "))
        ele = input("Enter element: ")
        linked_list.insert(pos, ele)
        print("List: ", linked_list)

    elif ch == 3:
        if len(linked_list) == 0: 
            print("The list is empty!") 
        else:
            print("List: ", linked_list)

    elif ch == 4:  
        if len(linked_list) == 0: 
            print("The list is empty!") 
        else:
            print("\nDeleted: ")  
            print(linked_list.pop())
            print("List: ", linked_list)

    elif ch == 5:  
        if len(linked_list) == 0: 
            print("The list is empty!") 
        else:
            ele = input("Enter element: ")
            print("\nDeleted: ")  
            print(linked_list.remove(ele))
            print("List: ", linked_list)

    elif ch == 6:
        break

    else:  
        print("ERR: Invalid Choice!")