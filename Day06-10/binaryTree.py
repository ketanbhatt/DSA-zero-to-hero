'''

Name:    Binary Tree                                
Purpose: Various operations on binary tree                                      
Created by: TigerApps                                 

'''

import random
import sys
	

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

	# preorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def preOrder(self,node):
		if not node:
			return
		print node,
		self.preOrder(node.left)
		self.preOrder(node.right)
	
	# inorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def inOrder(self,node):
		if not node:
			return
		self.inOrder(node.left)
		print node,
		self.inOrder(node.right)

	# postorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def postOrder(self,node):
		if not node:
			return
		self.postOrder(node.left)
		self.postOrder(node.right)
		print node,

	# levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def levelOrder(self,node):
		for i in range(self.height(node)):
			#print ""    #uncomment to print different levels in different lines
			self.__levelOrder(node,i)
			print " ",
			
	def __levelOrder(self,node,height):
		if not node:
			return
		if height==0:
			print node,
		else:
			self.__levelOrder(node.left,height-1)
			self.__levelOrder(node.right,height-1)

	# reverse levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def levelOrderR(self,node):
		for i in range(self.height(node),-1,-1):
			#print ""    #uncomment to print different levels in different lines
			self.__levelOrderR(node,i)
			print " ",
			
	def __levelOrderR(self,node,height):
		if not node:
			return
		if height==0:
			print node,
		else:
			self.__levelOrderR(node.left,height-1)
			self.__levelOrderR(node.right,height-1)

	# verticalorder traversal of the binary tree
	# time complexity: O(n) hash map operations time complexity: O(1)
	# space complexity: O(n)
	def verticalOrder(self,node):
		myhash = {}
		self.__verticalOrder(self.root,myhash,0)
		hdmin = min(myhash.keys())
		hdmax = max(myhash.keys())
		for hd in range(hdmin,hdmax+1):
			for node in range(len(myhash[hd])):
				print myhash[hd][node],
			print "",

	def __verticalOrder(self,node,myhash,hd):
		if not node:
			return
		self.__verticalOrder(node.left,myhash,hd-1)
		try:
			myhash[hd].append(node)
		except:
			myhash[hd] = [node]
		self.__verticalOrder(node.right,myhash,hd+1)


	# topview of the binary tree
	# time complexity: O(n) hash map,queue operations time complexity: O(1)
	# space complexity: O(n)
	def topView(self,node):
		minhd = 0
		maxhd = 0
		myhash = {}
		myqueue = [[node,0]]
		myhash[0] = node
		while myqueue:
			node,hd = myqueue.pop(0)
			
			if node:
				if hd<minhd:
					myhash[hd] = node
					minhd = hd
				elif hd>maxhd:
					myhash[hd] = node
					maxhd = hd
				myqueue.append([node.left,hd-1])
				myqueue.append([node.right,hd+1])
		hdmin = min(myhash.keys())
		hdmax = max(myhash.keys())
		for hd in range(hdmin,hdmax+1):
			print myhash[hd],
			
	# leftview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def leftView(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.__leftView(node,0,levelvisited)

	def __leftView(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.__leftView(node.left,level+1,levelvisited)
		self.__leftView(node.right,level+1,levelvisited)

	# rightview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def rightView(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.__rightView(node,0,levelvisited)

	def __rightView(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.__rightView(node.right,level+1,levelvisited)
		self.__rightView(node.left,level+1,levelvisited)

	# bottomview of the binary tree
	# time complexity: O(n)
	# space complexity: O(n)
	def bottomView(self,node):
		myqueue = [[node,0]]
		myhash = {}
		while myqueue:
			node,hd = myqueue.pop(0)
			
			if node:
				myhash[hd] = node
				myqueue.append([node.left,hd-1])
				myqueue.append([node.right,hd+1])
				
		minhd = min(myhash.keys())
		maxhd = max(myhash.keys())
		for key in range(minhd,maxhd+1):
			print myhash[key],	

	
	# levelorder traversal in spiral way of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def spiral(self,node):
		right = False
		for i in range(self.height(node)):
			#print ""    #uncomment to print different levels in different lines
			self.__spiral(node,i,right)
			right = not right	
			print " ",
			
	def __spiral(self,node,height,right):
		if not node:
			return
		if height==0:
			print node,
		else:
			if right:
				self.__spiral(node.left,height-1,right)
				self.__spiral(node.right,height-1,right)
			else:
				self.__spiral(node.right,height-1,right)
				self.__spiral(node.left,height-1,right)


	# all leaf nodes of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def leaves(self,node):
		if not node:
			return 0
		if not node.left and not node.right:
			print node,
			return 1
		else:
			return self.leaves(node.left) + self.leaves(node.right)	

	# all root to leaf paths of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def paths(self,node,path):
		if not node:
			return
		path.append(node)
		if not node.left and not node.right:
			for n in path:
				print n,
			print
		else:
			self.paths(node.left,path)
			self.paths(node.right,path)	
		path.pop()

	# boundary of the binary tree
	# time complexity: O(n)
	# space complexity: O(n)
	def boundary(self,node):
		if not node:
			return
		curr = node
		while curr.left and curr.left:
			print curr,
			curr=curr.left
		self.leaves(self.root)
		stack = []
		curr = node.right
		while curr.right:
			stack.append(curr)
			curr=curr.right
		while stack:
			curr = stack.pop()
			print curr,

	# level of a node of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def level(self,node,item,level):
		if not node:
			return 0
		if node.data == item:
			return level
		else:
			return max(self.level(node.left,item,level+1),self.level(node.right,item,level+1))

	# check if all leaves are at same level
	# time complexity: O(n)
	# space complexity: O(1)
	def levelLeaf(self,node):
		leaf = []
		return self.__levelLeaf(node,leaf,0)

	def __levelLeaf(self,node,leaf,level):
		if not node.left and not node.right:
			if leaf == []:
				leaf.append(level)
				return True
			else:
				if level == leaf[0]:
					return True
				else:
					return False
		else:
			bool1 = True
			bool2 = True
			if node.left:
				bool1 = self.__levelLeaf(node.left,leaf,level+1)
			if node.right:
				bool2 = self.__levelLeaf(node.right,leaf,level+1)
			return bool1 and bool2

	# find min element in a binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def minNode(self,node,):
		if not node:
			return sys.maxint
		return min(self.minNode(node.left),node.data,self.minNode(node.right))
	
	# find max element in a binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def maxNode(self,node,):
		if not node:
			return -sys.maxint
		return max(self.maxNode(node.left),node.data,self.maxNode(node.right))

	# find diameter of a binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def diameter(self,node):
		dia = [0]
		self.__diameter(node,dia)
		return dia[0]
	
	def __diameter(self,node,dia):
		if not node:
			return 0
		ld = self.__diameter(node.left, dia)
		rd = self.__diameter(node.right, dia)

		if ld + rd +1 > dia[0]:
			dia[0] = ld + rd + 1
		return 1 + max(ld, rd)

	# find diameter of a binary tree
	# time complexity: O(n^2)
	# space complexity: O(1)
	def diameter2(self,node):
		if not node:
			return 0
		return max(self.diameter2(node.left), 1 + self.height(node.left) + \
			self.height(node.right) ,self.diameter2(node.right))
		
	# find maximum width of a binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def width(self,node,):
		if not node:
			return 0
		myqueue = []
		myqueue.append(node)
		maxWidth = 0
		while myqueue:
			temp = len(myqueue)
			maxWidth = max(temp,maxWidth)
			while temp:
				curr = myqueue.pop(0)
				if curr.left:
					myqueue.append(curr.left)
				if curr.right:
					myqueue.append(curr.right)
				temp -= 1
		return maxWidth

	
	# find leaf node closest to given node
	# time complexity: 
	# space complexity:
	def findClosest(self,node,data):
		pass

	# check if the binary tree is height balanced
	# time complexity: O(n)
	# space complexity: O(1)
	def balanced(self,node):
		return self.__balanced(node)[0]

	def __balanced(self,node):
		if not node:
			return True,0

		lbal,lh = self.__balanced(node.left)
		rbal,rh = self.__balanced(node.right)

		h = 1 + max(lh,rh)
		bal = True if abs(lh - rh) == 1 else False
		return bal,h

	def mirror(self,node):
		if not node:
			return
		self.mirror(node.left)
		self.mirror(node.right)
		node.left , node.right = node.right , node.left

# check if two binary trees are identical
# time complexity: O(n)
# space complexity: O(1)
def isIdentical(node,node2):
	if not node and not node2:
		return True
	elif not node or not node2:
		return False
	else:
		return node.data == node2.data and isIdentical(node.left,node2.left) and isIdentical(node.right,node2.right)

# check if a binary tree is a sub tree of another   
# time complexity: O(n^2)
# space complexity: O(1)
def isSubtree(node,node2):	#if node2 tree is subtree of node treee
	if not node2:
		return True
	if not node:
		return False

	if isIdentical(node,node2):
		return True
	return isSubtree(node.left,node2) or isSubtree(node.right,node2)




myTree = BinaryTree()

for i in range(9):
	myTree.insert(i) 


# myTree.root.left.left = myTree.Node(5)
# myTree.root.left.left.left = myTree.Node(15)
# myTree.root.left.right = myTree.Node(16)
# myTree.root.left.right.right = myTree.Node(50)
# myTree.root.left.right.right.right = myTree.Node(52)


print "Binary Tree"

print "Height:    ",myTree.height(myTree.root)

print "Size:      ",myTree.size(myTree.root)
	
print "Preorder Traversal:   	 ",
myTree.preOrder(myTree.root)
print

print "Inorder Traversal:    	 ",
myTree.inOrder(myTree.root)
print

print "Postorder Traversal:  	 ",
myTree.postOrder(myTree.root)
print

print "Level Order Traversal:   ",
myTree.levelOrder(myTree.root)
print

print "Reverse Level Order:   ",
myTree.levelOrderR(myTree.root)
print

print "Spiral Traversal:        ",
myTree.spiral(myTree.root)
print

myTree.mirror(myTree.root)
print "Mirror Level Order:      ",
myTree.levelOrder(myTree.root)
print
myTree.mirror(myTree.root)

print "Vertical Order Traversal:",
myTree.verticalOrder(myTree.root)
print

print "Boundary Traversal:      ",
myTree.boundary(myTree.root)
print

print "Top View:   ",
myTree.topView(myTree.root)
print

print "Left View:  ",
myTree.leftView(myTree.root)
print 

print "Right View: ",
myTree.rightView(myTree.root)
print ""

print "Bottom View:",
myTree.bottomView(myTree.root)
print ""

print "Leaves:     ",
leaf = myTree.leaves(myTree.root)
print
print "No. of Leaf Nodes: ",leaf

print "Root to Leaf Paths: "
myTree.paths(myTree.root,[])

print "Level Leaf:  ",myTree.levelLeaf(myTree.root)
print "Balanced:    ",myTree.balanced(myTree.root)

print "Min Element: ",myTree.minNode(myTree.root)
print "Max Element: ",myTree.maxNode(myTree.root)

print "Diameter:    ",myTree.diameter(myTree.root)

print "Max Width:   ",myTree.width(myTree.root)


