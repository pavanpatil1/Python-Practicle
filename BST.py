# Python program to demonstrate insert operation in binary search tree  
  
# A utility class that represents an individual node in a BST 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
  


r = Node("Man") 
insert(r,Node("hello")) 
insert(r,Node("hell")) 
insert(r,Node("Monkey")) 
insert(r,Node("Eight")) 
insert(r,Node("Elephant")) 
insert(r,Node("Hello")) 
  
# Print inoder traversal of the BST 
inorder(r) 
