
print("Atharva Auti Roll No. 1\nQueue Data Structure using Python\n")  

from queue import Queue 

queue = Queue();

while True:  
    print("""
1. Enqueue
2. Dequeue
3. Display
4. Exit
    """)
    ch = int(input("Enter your choice: "))  

    
    if ch == 1:   
        ele = input("Enter Element: ")
        queue.put(ele)
        print("Queue: ", queue.queue)

    elif ch == 2:
        if (queue.empty() == True):
            print("The queue is empty!") 
        else:    
            print("\nDeleted: ")  
            print(queue.get())
            print("Queue: ", queue.queue)

    elif ch == 3:
        if (queue.empty() == True):
            print("The queue is empty!") 
        else:
            print("Queue: ", queue.queue)

    elif ch == 4:  
        break  

    else:  
        print("ERR: Invalid Choice!")