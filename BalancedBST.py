class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None

def convert(list): 
	
	if not list: 
		return None
	mid = (len(list)) / 2
	root = Node(list[mid]) 
	root.left = convert(list[:mid]) 
	root.right = convert(list[mid+1:]) 
	return root 

def preOrder(node): 
	if not node: 
		return
	
	print node.data, 
	preOrder(node.left) 
	preOrder(node.right) 

list = [10,20,30,40,50] 
root = convert(list) 
print "PreOrder Traversal of Balanced Binary Search Tree: ", 
preOrder(root) 

