import random

# LinkedList object
class BinaryTree:
	def __init__(self):
		self.root = None

	# Node object
	class Node:
		def __init__(self,data):
			self.data = data
			self.left = None
			self.right = None

		def __str__(self):
			return str(self.data)	

	# insert in balanced way
	# time complexity: O(logn) queue operations time complexity: O(1)
	# space complexity: O(n)
	def insert(self,data):
		new = self.Node(data)
		if not self.root:
			self.root = new
			return
		queue = []
		queue.append(self.root)
		while True:
			curr = queue.pop(0)
			if not curr.left:
				curr.left = new
				break
			else:
				queue.append(curr.left)
			if not curr.right:
				curr.right = new
				break
			else:
				queue.append(curr.right)
		return


	# preorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def preorder(self,node):
		if not node:
			return
		print node.data,
		self.preorder(node.left)
		self.preorder(node.right)
	
	# inorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def inorder(self,node):
		if not node:
			return
		self.inorder(node.left)
		print node.data,
		self.inorder(node.right)

	# postorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def postorder(self,node):
		if not node:
			return
		self.postorder(node.left)
		self.postorder(node.right)
		print node.data,

	# levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def levelorder(self,node):
		for i in range(self.height(node)):
			#print ""    #uncomment to print different levels in different lines
			self.levelorder_h(node,i)
			print " ",
			
	def levelorder_h(self,node,height):
		if not node:
			return
		if height==0:
			print node,
		else:
			self.levelorder_h(node.left,height-1)
			self.levelorder_h(node.right,height-1)

	# verticalorder traversal of the binary tree
	# time complexity:
	# space complexity:
	def verticalorder(self,node):
		pass

	# topview of the binary tree
	# time complexity:
	# space complexity:
	def topview(self,node):
		pass

	# leftview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def leftview(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.leftview_h(node,0,levelvisited)

	def leftview_h(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.leftview_h(node.left,level+1,levelvisited)
		self.leftview_h(node.right,level+1,levelvisited)

	# rightview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def rightview(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.rightview_h(node,0,levelvisited)

	def rightview_h(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.rightview_h(node.right,level+1,levelvisited)
		self.rightview_h(node.left,level+1,levelvisited)
		

	# height of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def height(self,node):
		if not node:
			return 0
		return 1 + max(self.height(node.left),self.height(node.right))

	# size of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def size(self,node):
		if not node:
			return 0
		return self.size(node.left) + 1 + self.size(node.right)

mytree = BinaryTree()

for i in range(10):
	mytree.insert(i) 


print "Height: ",mytree.height(mytree.root)

print "Size:   ",mytree.size(mytree.root)
	
print "Preorder:   	  ",
mytree.preorder(mytree.root)
print ""

print "Inorder:    	  ",
mytree.inorder(mytree.root)
print ""

print "Postorder:  	  ",
mytree.postorder(mytree.root)
print ""

print "Verticalorder: ",
mytree.verticalorder(mytree.root)
print ""

print "Topview:  	  ",
mytree.topview(mytree.root)
print ""

print "Leftview: 	  ",
mytree.leftview(mytree.root)
print ""

print "Rightview: 	  ",
mytree.rightview(mytree.root)
print ""

print "Levelorder: 	  ",
mytree.levelorder(mytree.root)
print ""
