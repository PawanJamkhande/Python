### BINARY SEARCH ###
# def binary_search(arr, target, low, high):
#     """
#     Parameters:
#         arr (list): The sorted list to be searched.
#         target: The value to be searched for.
#         low (int): The lower index of the search interval.
#         high (int): The upper index of the search interval.
#     """
#     if low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binary_search(arr, target, mid + 1, high)
#         else:
#             return binary_search(arr, target, low, mid - 1)
#     else:
#         return -1

# # Example usage:
# arr = [2, 3, 4, 10, 40]
# target = 4
# result = binary_search(sorted(arr), target, 0, len(arr) - 1)
# if result != -1:
#     print(f"Binary Search: Element found at index {result}")
# else:
#     print("Binary Search: Element not found")

# class BinaryTree:
#     def __init__(self,data):
#         self.data = data #instance variable
#         self.children = [] #list to store the data 

#     def __str__(self,level =0):
#         ret = "  "* level + str(self.data)+"\n"
#         for child in self.children:
#             ret+= child.__str__(level+1)
#         return ret
#     def addChild(self,treeNode):
#         self.children.append(treeNode)

# node_1=BinaryTree('Drinks')
# node_2=BinaryTree('Hot')
# node_3=BinaryTree('Cold')
# node_4=BinaryTree('Tea')
# node_5=BinaryTree('Coffee')
# node_6=BinaryTree('Alcoholic')
# node_7=BinaryTree('Non-Alcoholic')
# node_8=BinaryTree('Magic-Moment')
# node_9=BinaryTree('Dr.Brandy')
# node_10=BinaryTree('Applejuice')
# node_11=BinaryTree('Bananajuice')
# node_1.addChild(node_2)
# node_1.addChild(node_3)
# node_2.addChild(node_4)
# node_2.addChild(node_5)
# node_3.addChild(node_6)
# node_3.addChild(node_7)
# node_6.addChild(node_8)
# node_6.addChild(node_9)
# node_7.addChild(node_10)
# node_7.addChild(node_11)

# print(node_1)

###SEARCHING ALGORITHMS
#1)DFS - *Preorder *Inorder *Postorder 2)BFS
##For preorder
# class BinaryTree:
#     def __init__(self, data):
#         self.data = data  # Instance variable
#         self.children = []

#     def __str__(self, level=0):
#         ret = '  ' * level + str(self.data) + '\n'
#         for child in self.children:
#             ret += child.__str__(level + 1)  # Correct recursion call
#         return ret

#     # Method to add a child node
#     def add_child(self, treenode):
#         self.children.append(treenode)

#     # Preorder Traversal (Root -> Children)
#     def preorder(self):
#         print(self.data, end=' ')  # Visit the root first
#         for child in self.children:
#             child.preorder()

#     # Inorder Traversal (First child -> Root -> Other children)
#     def inorder(self):
#         if self.children:  # If there are children, process the first child first
#             self.children[0].inorder()
#         print(self.data, end=' ')  # Visit the root
#         for child in self.children[1:]:  # Process remaining children
#             child.inorder()

#     # Postorder Traversal (Children -> Root)
#     def postorder(self):
#         for child in self.children:
#             child.postorder()
#         print(self.data, end=' ')  # Visit the root last

# # Creating nodes
# node_1 = BinaryTree('drinks')
# node_2 = BinaryTree('hot')
# node_3 = BinaryTree('cold')
# node_4 = BinaryTree('tea')
# node_5 = BinaryTree('coffee')
# node_6 = BinaryTree('alcoholic')
# node_7 = BinaryTree('non-alcoholic')

# # Adding child nodes
# node_1.add_child(node_2)
# node_1.add_child(node_3)
# node_2.add_child(node_4)
# node_2.add_child(node_5)
# node_3.add_child(node_6)
# node_3.add_child(node_7)

# # Printing tree structure
# print("Tree Structure:")
# print(node_1)

# # Performing DFS Traversals
# print("\nPreorder Traversal:")
# node_1.preorder()

# print("\n\nInorder Traversal:")
# node_1.inorder()

# print("\n\nPostorder Traversal:")
# node_1.postorder()

# import queue

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# newBT = TreeNode("Drinks")
# leftChild =TreeNode("Hot")
# tea = TreeNode("Tea")
# coffee = TreeNode("coffee")
# leftChild.leftChild = tea
# leftChild.rightChild = coffee
# rightChild = TreeNode("Cold")
# newBT.leftChild  = leftChild
# newBT.rightChild = rightChild
# print(newBT)
# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return 
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)

# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return 
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)
# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)
# inOrderTraversal(newBT)
# print('inorder done')
# postOrderTraversal(newBT)
# print('postorder done')
# preOrderTraversal(newBT)
# print('preorder done')

# mylist=[[100,1333,187,122],
#         [122,232,221,111],
#         [223,565,245,764]]
# newlist=[]
# for i in range (3):
#     j=0
#     max =mylist[i][j]
#     for j in range(4):
#         c_max=mylist[i][j]
#         if max<c_max:
#             max=c_max
#     newlist.append(max)
# print(newlist)

# row = int(input("Enter the number of rows: "))
# colomn = int(input("Enter the number of colomns: "))

# matrix=[]
# for i in range(row):
#     a=[]
#     for j in range(colomn):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)


### shift * to the left ###
# s = input("Enter the string: ")
# c = s.count('*')
# s = s.replace('*','')
# for i in range(c):
#     s = '*'+s
# print(s)

## GRAPH ##

# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False
    
#     def add_edge(self,ver1,ver2):
#         if ver1 in self.adjacency_list.keys():
#             self.adjacency_list[ver1].append(ver2)
#             self.adjacency_list[ver2].append(ver1)
#             return True
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])

    
# mygraph = Graph()
# mygraph.add_vertex("A")
# mygraph.add_vertex("B")
# mygraph.add_vertex("C")
# mygraph.add_vertex("D")
# mygraph.add_vertex("E")
# mygraph.add_edge("A","B")
# mygraph.add_edge("A","C")
# mygraph.add_edge("A","D")
# mygraph.add_edge("B","E")
# mygraph.add_edge("D","C")
# mygraph.add_edge("E","D")
# mygraph.print_graph()



