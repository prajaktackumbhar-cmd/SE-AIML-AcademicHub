SIZE = 5
queue = []

def enqueue():
    if len(queue) == SIZE:
        print("Queue Overflow!")
    else:
        value = int(input("Enter value: "))
        queue.append(value)
        print("Element inserted successfully.")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow!")
    else:
        print("Deleted element:", queue.pop(0))

def peek():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Front element:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Queue elements are:")
        for element in queue:
            print(element, end=" ")
        print()

while True:
    print("\n--- QUEUE ADT MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
