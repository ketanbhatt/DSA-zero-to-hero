'''

Name:    Binary Tree                                
Purpose: Various operations on a binary tree                                      
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

	# insert in a complete binary tree iterative
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
	# space complexity: O(h)
	def height(self,node):
		if not node:
			return 0
		return 1 + max(self.height(node.left),self.height(node.right))
	# height of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(w)
	def height_i(self,node):
		myqueue = []
		myqueue.append([node,1])
		maxht = 0
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr,ht = myqueue.pop(0)
				if curr:
					maxht = max(maxht,ht)
					myqueue.append([curr.left,ht+1])
					myqueue.append([curr.right,ht+1])
				temp -= 1
		return maxht

	# size of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def size(self,node):
		if not node:
			return 0
		return self.size(node.left) + 1 + self.size(node.right)
	# size of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(w)
	def size_i(self,node):
		myqueue = []
		myqueue.append(node)
		sz = 0
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr = myqueue.pop(0)
				if curr:
					sz += 1
					myqueue.append(curr.left)
					myqueue.append(curr.right)
				temp -= 1
		return sz


	# preorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def preOrder(self,node):
		if not node:
			return
		print node,
		self.preOrder(node.left)
		self.preOrder(node.right)
	# preorder traversal of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def preOrder_i(self,node):
		mystack = []
		mystack.append(node)
		pre = []
		while mystack:
			curr = mystack.pop()
			if curr:
				pre.append(curr)
				mystack.append(curr.right)
				mystack.append(curr.left)
		return pre

	
	# inorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def inOrder(self,node):
		if not node:
			return
		self.inOrder(node.left)
		print node,
		self.inOrder(node.right)
	# inorder traversal of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def inOrder_i(self,node):
		curr = node
		mystack = []
		mystack.append(curr)
		inO = []
		while mystack:
			while curr.left:
				mystack.append(curr.left)
				curr = curr.left
			while not curr.right and mystack:
				curr = mystack.pop()
				inO.append(curr)
			if curr.right:
				curr = curr.right
				mystack.append(curr)
		return inO


	# postorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def postOrder(self,node):
		if not node:
			return
		self.postOrder(node.left)
		self.postOrder(node.right)
		print node,
	# postorder traversal of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def postOrder_i(self,node):
		mystack = []
		mystack.append(node)
		post = []
		while mystack:
			curr = mystack.pop()
			if curr:
				post.append(curr)
				mystack.append(curr.left)
				mystack.append(curr.right)
		return post[::-1]

	# levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
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
	# levelorder traversal of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def levelOrder_i(self,node):
		myqueue = []
		myqueue.append(node)
		level = []
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr = myqueue.pop(0)
				if curr:
					level.append(curr)
					myqueue.append(curr.left)
					myqueue.append(curr.right)
				temp -= 1
			level.append(" ")
		return level

	# reverse levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
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
	# reverse levelorder traversal of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def levelOrderR_i(self,node):
		myqueue = []
		myqueue.append(node)
		level = []
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr = myqueue.pop(0)
				if curr:
					level.append(curr)
					myqueue.append(curr.right)
					myqueue.append(curr.left)
				temp -= 1
			level.append(" ")
		while level[-1]==" ":
			level = level[:-1]
		level.append(" ")
		return level[::-1]

	# levelorder traversal in spiral way of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
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
	# levelorder traversal in spiral way of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def spiral_i(self,node):
		myqueue = []
		myqueue.append(node)
		spiral = []
		right = False
		while myqueue:
			temp = len(myqueue)
			if right:
				spiral.extend(myqueue[:])
			else:
				spiral.extend(myqueue[::-1])
			right = not right
			while temp:
				curr = myqueue.pop(0)
				if curr.left:
					myqueue.append(curr.left)
				if curr.right:
					myqueue.append(curr.right)
				temp -= 1
			spiral.append(" ")
		return spiral

	# verticalorder traversal of the binary tree
	# time complexity: O(n) hash map operations time complexity: O(1)
	# space complexity: O(n+h)
	def verticalOrder(self,node):
		myhash = {}
		self.__verticalOrder(self.root,myhash,0)
		for hd in sorted(myhash.keys()):
			for node in range(len(myhash[hd])):
				print myhash[hd][node],
			print " ",
	def __verticalOrder(self,node,myhash,hd):
		if not node:
			return
		try:
			myhash[hd].append(node)
		except:
			myhash[hd] = [node]
		self.__verticalOrder(node.left,myhash,hd-1)
		self.__verticalOrder(node.right,myhash,hd+1)
	# verticalorder traversal of the binary tree iterative
	# time complexity: O(n) hash map operations time complexity: O(1)
	# space complexity: O(n+w)
	def verticalOrder_i(self,node):
		myhash = {}
		myqueue = []
		myqueue.append([node,0])
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr,hd = myqueue.pop(0)
				if curr:
					if hd in myhash.keys():
						myhash[hd].append(curr)
					else:
						myhash[hd] = [curr]
					myqueue.append([curr.left,hd-1])
					myqueue.append([curr.right,hd+1])
				temp -= 1
		vertical = []
		for hd in sorted(myhash.keys()):
			for node in range(len(myhash[hd])):
				vertical.append(myhash[hd][node])
			vertical.append(" ")
		return vertical
	
	# boundary of the binary tree iterative
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

	# topview of the binary tree iterative
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
		for hd in sorted(myhash.keys()):
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

	# bottomview of the binary tree iterative
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
		for hd in sorted(myhash.keys()):
			print myhash[hd],
		

	# all leaf nodes of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def leaves(self,node):
		if not node:
			return 0
		if not node.left and not node.right:
			print node,
			return 1
		else:
			return self.leaves(node.left) + self.leaves(node.right)
	# all leaf nodes of the binary tree iterative
	# time complexity: O(n)
	# space complexity: O(n+w)
	def leaves_i(self,node):
		myqueue = []
		myqueue.append(node)
		leaves = []
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr = myqueue.pop(0)
				if curr:
					if not curr.left and not curr.right:
						leaves.append(curr)
					myqueue.append(curr.left)
					myqueue.append(curr.right)
				temp -= 1
		return leaves

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

	# level of a node of the binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def level(self,node,item,level):
		if not node:
			return 0
		if node.data == item:
			return level
		else:
			return max(self.level(node.left,item,level+1),self.level(node.right,item,level+1))

	# check if all leaves are at same level
	# time complexity: O(n)
	# space complexity: O(h)
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
	# space complexity: O(h)
	def minNode(self,node,):
		if not node:
			return sys.maxint
		return min(self.minNode(node.left),node.data,self.minNode(node.right))
	
	# find max element in a binary tree
	# time complexity: O(n)
	# space complexity: O(h)
	def maxNode(self,node,):
		if not node:
			return -sys.maxint
		return max(self.maxNode(node.left),node.data,self.maxNode(node.right))

	# find diameter of a binary tree
	# time complexity: O(n)
	# space complexity: O(h)
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
	# space complexity: O(h)
	def diameter2(self,node):
		if not node:
			return 0
		return max(self.diameter2(node.left), 1 + self.height(node.left) + \
			self.height(node.right) ,self.diameter2(node.right))
		
	# find maximum width of a binary tree iterative
	# time complexity: O(n)
	# space complexity: O(w)
	def width(self,node):
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

	
	# check if the binary tree is height balanced
	# time complexity: O(n)
	# space complexity: O(h)
	def isBalanced(self,node):
		return self.__isBalanced(node)[0]
	def __isBalanced(self,node):
		if not node:
			return True,0
		lbal,lh = self.__isBalanced(node.left)
		rbal,rh = self.__isBalanced(node.right)
		h = 1 + max(lh,rh)
		bal = True if abs(lh - rh) < 2 else False
		return bal,h

	# check if the binary tree is complete
	# time complexity: O(n)
	# space complexity: O(w)
	def isComplete(self,node):
		myqueue = []
		myqueue.append(node)
		foundNone = False
		while myqueue:
			temp = len(myqueue)
			while temp:
				curr = myqueue.pop(0)
				if curr:
					if foundNone:
						return False
					myqueue.append(curr.left)
					myqueue.append(curr.right)
				else:
					foundNone = True
				temp -= 1
		return True

	# check if the binary tree is a sum tree
	# time complexity: O(n)
	# space complexity: O(h)
	def isSumTree(self,node):
		if not node or not node.left and not node.right:
			return True
		ls = self.__Sum(node.left)
		rs = self.__Sum(node.right)
		return self.isSumTree(node.left) and node.data == ls + rs and self.isSumTree(node.right) 
	def __Sum(self,node):
		if not node: 
			return 0
		return self.__Sum(node.left) + node.data + self.__Sum(node.right)

	# convert a binary tree to its mirror tree
	# time complexity: O(n)
	# space complexity: O(h)
	def mirror(self,node):
		if not node:
			return
		self.mirror(node.left)
		self.mirror(node.right)
		node.left , node.right = node.right , node.left

# check if two binary trees are identical
# time complexity: O(n)
# space complexity: O(h)
def isIdentical(node,node2):
	if not node and not node2:
		return True
	elif not node or not node2:
		return False
	else:
		return node.data == node2.data and isIdentical(node.left,node2.left) and isIdentical(node.right,node2.right)

# check if a binary tree is a sub tree of another   
# time complexity: O(n^2)
# space complexity: O(h)
def isSubtree(node,node2):	#if node2 tree is subtree of node treee
	if not node2:
		return True
	if not node:
		return False

	if isIdentical(node,node2):
		return True
	return isSubtree(node.left,node2) or isSubtree(node.right,node2)


# to print a list of nodes
# time complexity: O(n)
# space complexity: O(1)
def myprint(list):
	for node in list:
		print node,
	print


myTree = BinaryTree()

for i in range(7):
	myTree.insert(i) 


print "Binary Tree"

print "Height:    ",myTree.height(myTree.root)
print "Height:    ",myTree.height_i(myTree.root)

print "Size:      ",myTree.size(myTree.root)
print "Size:      ",myTree.size_i(myTree.root)
	

# print "Preorder Traversal:   	 ",
# myTree.preOrder(myTree.root)
#print
print "Preorder Traversal:   	 ",
myprint(myTree.preOrder_i(myTree.root))

# print "Inorder Traversal:    	 ",
# myTree.inOrder(myTree.root)
# print
print "Inorder Traversal:   	 ",
myprint(myTree.inOrder_i(myTree.root))

# print "Postorder Traversal:  	 ",
# myTree.postOrder(myTree.root)
# print
print "Postorder Traversal:   	 ",
myprint(myTree.postOrder_i(myTree.root))


# print "Level Order Traversal:   ",
# myTree.levelOrder(myTree.root)
# print
print "Level Order Traversal:   ",
myprint(myTree.levelOrder_i(myTree.root))

# print "Reverse Level Order:   ",
# myTree.levelOrderR(myTree.root)
# print
print "Reverse Level Order:   ",
myprint(myTree.levelOrderR_i(myTree.root))

# print "Spiral Traversal:        ",
# myTree.spiral(myTree.root)
# print
print "Spiral Traversal:        ",
myprint(myTree.spiral_i(myTree.root))

# print "Vertical Order Traversal:",
# myTree.verticalOrder(myTree.root)
# print
print "Vertical Order Traversal:",
myprint(myTree.verticalOrder_i(myTree.root))

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


# print "Leaves:     ",
# leaf = myTree.leaves(myTree.root)
# print
# print "No. of Leaf Nodes: ",leaf
leaves = myTree.leaves_i(myTree.root)
print "No. of Leaf Nodes:",len(leaves)
print "Leaves:     ",
myprint(leaves)


print "Root to Leaf Paths: "
myTree.paths(myTree.root,[])

print "Level Leaf:  ",myTree.levelLeaf(myTree.root)
print "Balanced:    ",myTree.isBalanced(myTree.root)
print "Complete:    ",myTree.isComplete(myTree.root)
print "Sum Tree:    ",myTree.isSumTree(myTree.root)

print "Min Element: ",myTree.minNode(myTree.root)
print "Max Element: ",myTree.maxNode(myTree.root)

print "Diameter:    ",myTree.diameter(myTree.root)

print "Max Width:   ",myTree.width(myTree.root)

myTree.mirror(myTree.root)
print "Mirror Level Order:      ",
myTree.levelOrder(myTree.root)
print
myTree.mirror(myTree.root)

