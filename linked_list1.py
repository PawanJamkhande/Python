
# ## this is good for single operation on linked list 
# class Node:
#     def __init__(self,value):
#         self.data= value #instance variable
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

# linkObj = Linkedlist() #created obj for linkedlist class
# linkObj.head=Node(10) #created the obj from linkedlist class to call and assign value to Node class method
# second=Node(20)
# third =Node(30)
# #we have created nodes now and every node has assign their own space 
# #connection conecting the nodes that hvae created
# linkObj.head.next=second
# second.next=third

# while linkObj.head is not None:
#     # print(linkObj.head.data,' => ',linkObj.head.next,end=" ")  #print address of the next node
#     print(linkObj.head.data,' => ',end=" ") #prints only nodes

#     linkObj.head = linkObj.head.next #o/p -> 10  =>  20  =>  30  =>  %


import sys
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    #add node
    def addNode(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node 
            self.tail = node 

    #add at beginning
    def addNodeBeginning(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node    

    #add at the end
    def addNodeEnd(self,value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    #in between
    #add before the node
    
    # def addBeforeNode(self, value, before_value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         print("The list is empty.")
    #         return

    #     if self.head.data == before_value:
    #         new_node.next = self.head
    #         self.head = new_node
    #         return

    #     current = self.head
    #     while current.next is not None and current.next.data != before_value:
    #         current = current.next

    #     if current.next is None:
    #         print(f"Node with value {before_value} not found.")
    #     else:
    #         new_node.next = current.next
    #         current.next = new_node

    #node in between
    def addNodeBetween(self,value,index):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                if temp.next is None:
                    print("Index out of bound")
                    return
                temp = temp.next
            node.next = temp.next
            temp.next = node
    
    #display 
    def displayNode(self):
        while self.head is not None:
            print(self.head.data,'->',end=" ")
            self.head = self.head.next
        print(None)


            


if __name__ == '__main__':
    object = Linkedlist() #linkedlist object created
    #menu driven options
while True:
        print('1. Add Node Linkedlist :')
        print('2. Add Node in Beginning :')
        print('3. Add Node in Between :')
        print('4. Add Node in End :')
        print('5. Display Linkedlist :')
        print('6. Exit :')

        ch = int(input("Enter your choice: "))
        if ch == 1:
            value = int(input("Enter the element to be added: "))
            object.addNode(value)
            print("Node added successfully in a single linkedlist")
        elif ch == 2:
            value = int(input("Enter value to add node in beginning"))
            object.addNodeBeginning(value)
            print("Node added successfully at Beginning")
        elif ch == 3:
            value = int(input("Enter the value to be added: "))
            index = int(input("Enter the position at which you want to add the node: "))
            object.addNodeBetween(value,index)
            print("Value is added successfully")
        elif ch ==4:
            value = int(input("Enter the value to be added at the end of list"))
            object.addNodeEnd(value)
            print("Node added successfully at the end of the list")
        elif ch == 5:
            object.displayNode()
        
        elif ch == 6:
            sys.exit()

        else:
            print("You have entered invalid option")
            


