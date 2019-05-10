from random import randint

class Node(object):
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None
    
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, parent=None):
        if parent is None:
            parent = self.root
        if self.root is None:
            self.root = Node(key)
            print("Added", key, "as root node")
        else:
            if key > parent.key:                                            # Traverse the right sub-tree if key > current node
                if parent.right is None:
                    print("\nAdding", key,"to", parent.key, "\'s right")
                    parent.right = Node(key)
                else:
                    parent = parent.right
                    self.insert(key, parent)
            else:                                                           # Traverse the left sub-tree if key < current node
                if parent.left is None:         
                    print("\nAdding", key,"to", parent.key, "\'s left")
                    parent.left = Node(key)
                else:
                    parent = parent.left
                    self.insert(key, parent)
    
    def remove(self, key, parent=None):
        if self.root is None:
            return None
        elif parent is None:
            parent = self.root
            
        if key < parent.key:
            if parent.left is None:
                print("Not present")
            else:
                parent.left = self.remove(key, parent.left)             # if key < current node, traverse the left sub-tree
        elif key > parent.key:
            if parent.right is None:
                print("Not present")
            else:
                parent.right = self.remove(key, parent.right)           # if key > current node, traverse the right sub-tree
        elif key == parent.key:                                                       # key found
            if parent.left is None:                                 # base case: if node has no child or 1 child
                temp = parent.right
                parent = None
                return temp
            
            elif parent.right is None:
                temp = parent.left
                parent = None
                return temp
            
            else:                                                   # if node has 2 child, replace key to be removed with its successor
                temp = self.successor(parent)
                parent.key = temp.key
                parent.right = self.remove(temp.key, parent.right)
        return parent

    def search(self, key, parent=None):
        if parent is None:
            if self.root is None:
                return None
            if self.root == key:
                return self.root
            parent = self.root
        if parent.key == key:
            return parent
        if key > parent.key:
            if parent.right is None:
                return None
            return self.search(key, parent.right)
        elif key < parent.key:
            if parent.left is None:
                return None
            return self.search(key, parent.left)  

    def successor(self, key):
        '''method to find the successor of the given key'''
        if isinstance(key, Node):
            node = self.search(key.key)
        else:
            node = self.search(key)
        succ = node.right
        if succ is not None:
            while succ.left:
                succ = succ.left
        return succ

    def inorder(self, node=1):
        '''method to print BST inorder (left, root, right)'''
        if node == 1:
            node = self.root
            print("\nBST is: (inorder)\n")
        if node:
            self.inorder(node.left)
            print(node.key, end=", ")
            self.inorder(node.right)


def main():
    bst = BST()
    height = 4
    n = 2**height - 1
    for _ in range(n):
        bst.insert(randint(1, 100))
    bst.inorder()

    bst.remove(int(input("\n")))
    bst.inorder()
    bst.remove(int(input("\n")))
    bst.inorder()


if __name__ == "__main__":
    main()