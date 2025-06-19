## STACK IMPLEMENTATION WITH SIZE ##
import sys
class Stack:
    def __init__(self,size):
        self.stacklist=[] #List representing stack
        self.maxsize = size 

    #Push
    def push(self,value):
        if self.isFull():
            print("stack is full")
        else:
            self.stacklist.append(value) #to add value in stack
    #display
    def displayStack(self):
        print(self.stacklist)
    #pop
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.stacklist.pop())
    #isEmpty
    def isEmpty(self):
        if self.stacklist == []:
            return True
        else:
            return False
    #PEEK
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stacklist[-1])
    #Delete
    def delete(self):
        self.stacklist=[]

    #isFull
    def isFull(self):
        if len(self.stacklist) == self.maxsize:
            return True
        else:
            return False


size = int(input("Enter the size of the stack: "))
obj = Stack(size)
print("stack has created")
while True:
     print("1. Push Operation: ")
     print("2. Pop Operation: ")
     print("3. PEEK Operation: ")
     print("4. isEmpty Operation: ")
     print("5. Delete Operation: ")
     print("6. Display Operation: ")
     print("7. Exit Operation: ")
     print("8. isFull")
    #  print("Push Operation: ")
     ch = int(input("Enter your choice: "))

     if ch ==1:
         value = int(input("Enter the element for stack: "))
         obj.push(value)

     elif ch == 2:
         obj.pop()
     
     elif ch == 3:
         obj.peek()
     
     elif ch == 4:
         print(obj.isEmpty())

     elif ch ==5 :
         obj.delete()

     elif ch == 6:
         obj.displayStack()
    
     elif ch == 7:
         sys.exit()

     elif ch == 8:
         print(obj.isFull())

     else:
         print("You have entered invalid choice: ")

     
     




     