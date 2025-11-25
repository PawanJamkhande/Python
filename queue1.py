import sys

class Queue:
    def __init__(self):
        self.queuelist = []  # List representing queue

    # Enqueue
    def enqueue(self, value):
        self.queuelist.append(value)  # to add value in queue

    # Display
    def displayQueue(self):
        print(self.queuelist)

    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.queuelist.pop(0))

    # isEmpty
    def isEmpty(self):
        return len(self.queuelist) == 0

    # Peek
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queuelist[0])

    # Delete
    def delete(self):
        self.queuelist = []

obj = Queue()
print("Queue has been created")
while True:
    print("1. Enqueue Operation: ")
    print("2. Dequeue Operation: ")
    print("3. PEEK Operation: ")
    print("4. isEmpty Operation: ")
    print("5. Delete Operation: ")
    print("6. Display Operation: ")
    print("7. Exit Operation: ")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        value = int(input("Enter the element for queue: "))
        obj.enqueue(value)

    elif ch == 2:
        obj.dequeue()

    elif ch == 3:
        obj.peek()

    elif ch == 4:
        print(obj.isEmpty())

    elif ch == 5:
        obj.delete()

    elif ch == 6:
        obj.displayQueue()

    elif ch == 7:
        sys.exit()

    else:
        print("You have entered an invalid choice: ")


# DOUBLE ENDED QUEUE ##
import collections
de = collections.deque([1,2,3])
print(de)
de.append(4) #added from the right
print(de)
de.appendleft(5) #added from the left
print(de)
de = collections.deque([5,1,2,3,4])
print(de)
de.pop()  #remove element from right
print(de)
de.popleft() #remove left element 
print(de)
