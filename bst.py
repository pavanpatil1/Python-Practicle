# Python code to convert a sorted array in  binary tree node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.left = None
		self.right = None

# function to convert sorted array to a BST
def sortedArrayToBST(arr): 
	
	if not arr: 
		return None

	# find middle 
	mid = (len(arr)) / 2
	
	# assign mid as root 
	root = Node(arr[mid]) 
	
	# left subtree of root has all values <arr[mid] 
	root.left = sortedArrayToBST(arr[:mid]) 
	
	# right subtree of root has all  values >arr[mid] 
	root.right = sortedArrayToBST(arr[mid+1:]) 
	return root 

# TRANSVERSE OF BST PREORDER
def bstorder(node): 
	if not node: 
		return
	
	print node.data, 
	bstorder(node.left) 
	bstorder(node.right) 

# driver program to test above function 
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
print ("bstorder") 
bstorder(root) 