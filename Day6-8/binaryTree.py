'''

Name:    Binary Tree                                
Purpose: Various operations on binary tree                                      
Created by: TigerApps                                 

'''

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
	def preOrder(self,node):
		if not node:
			return
		print node.data,
		self.preOrder(node.left)
		self.preOrder(node.right)
	
	# inorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def inOrder(self,node):
		if not node:
			return
		self.inOrder(node.left)
		print node.data,
		self.inOrder(node.right)

	# postorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def postOrder(self,node):
		if not node:
			return
		self.postOrder(node.left)
		self.postOrder(node.right)
		print node.data,

	# levelorder traversal of the binary tree
	# time complexity: O(n)
	# space complexity: O(1)
	def levelOrder(self,node):
		for i in range(self.height(node)):
			#print ""    #uncomment to print different levels in different lines
			self.levelOrder_h(node,i)
			print " ",
			
	def levelOrder_h(self,node,height):
		if not node:
			return
		if height==0:
			print node,
		else:
			self.levelOrder_h(node.left,height-1)
			self.levelOrder_h(node.right,height-1)

	# verticalorder traversal of the binary tree
	# time complexity: O(n) hash map operations time complexity: O(1)
	# space complexity: O(n)
	def verticalOrder(self,node):
		myhash = {}
		self.verticalOrder_h(self.root,myhash,0)
		hdmin = min(myhash.keys())
		hdmax = max(myhash.keys())
		for hd in range(hdmin,hdmax+1):
			for node in range(len(myhash[hd])):
				print myhash[hd][node],
			print "",

	def verticalOrder_h(self,node,myhash,hd):
		if not node:
			return
		self.verticalOrder_h(node.left,myhash,hd-1)
		try:
			myhash[hd].append(node)
		except:
			myhash[hd] = [node]
			
		self.verticalOrder_h(node.right,myhash,hd+1)


	# topview of the binary tree
	# time complexity: O(n) hash map operations time complexity: O(1)
	# space complexity: O(n)
	def topView(self,node):
		minhd = 0
		maxhd = 0
		myqueue = [[node,0]]
		print node,
		while myqueue:
			node,hd = myqueue.pop(0)
			
			if node:
				if hd<minhd:
					print node,
					minhd = hd
				elif hd>maxhd:
					print node,
					maxhd = hd
				myqueue.append([node.left,hd-1])
				myqueue.append([node.right,hd+1])





	# leftview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def leftView(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.leftView_h(node,0,levelvisited)

	def leftView_h(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.leftView_h(node.left,level+1,levelvisited)
		self.leftView_h(node.right,level+1,levelvisited)

	# rightview of the binary tree
	# time complexity: O(n)
	# space complexity: O(Log(n))
	def rightView(self,node):
		levelvisited = []
		for i in range(self.height(self.root)):
			levelvisited.append(0)
		self.rightView_h(node,0,levelvisited)

	def rightView_h(self,node,level,levelvisited):
		if not node:
			return
		if not levelvisited[level]:
			print node,
			levelvisited[level] = 1
		self.rightView_h(node.right,level+1,levelvisited)
		self.rightView_h(node.left,level+1,levelvisited)
		

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

myTree = BinaryTree()

for i in range(10):
	myTree.insert(i) 

print "Binary Tree"
print "Height:    ",myTree.height(myTree.root)

print "Size:      ",myTree.size(myTree.root)
	
print "Preorder Traversal:   	 ",
myTree.preOrder(myTree.root)
print ""

print "Inorder Traversal:    	 ",
myTree.inOrder(myTree.root)
print ""

print "Postorder Traversal:  	 ",
myTree.postOrder(myTree.root)
print ""

print "Level Order Traversal: 	 ",
myTree.levelOrder(myTree.root)
print ""

print "Vertical Order Traversal:",
myTree.verticalOrder(myTree.root)
print ""

print "Top View:   ",
myTree.topView(myTree.root)
print ""

print "Left View:  ",
myTree.leftView(myTree.root)
print ""

print "Right View: ",
myTree.rightView(myTree.root)
print ""
