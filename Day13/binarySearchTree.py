'''

Name:    Binary Search Tree                                
Purpose: Various operations on a binary search tree                                      
Created by: TigerApps                                 

'''

import random
import sys
	

# BinarySearchTree object
class BinarySearchTree:
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

	# inorder traversal of the binary tree recursive
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
		if not node:
			return []
		curr = node
		mystack = []
		mystack.append(curr)
		inO = []
		while mystack:
			while curr.left:
				mystack.append(curr.left)
				curr = curr.left
			curr = mystack.pop()
			inO.append(curr)
			while not curr.right and mystack:
				curr = mystack.pop()
				inO.append(curr)
			if curr.right:
				curr = curr.right
				mystack.append(curr)
		return inO

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


	# insert in a binary search tree recursive
	# time complexity: O(h)
	# space complexity: O(h)
	def insert(self,node,data):
		if not node:
			return self.Node(data)
		if data < node.data:
			node.left = self.insert(node.left,data)
		elif data == node.data:
			pass
		else:
			node.right = self.insert(node.right,data)
		return node
	# insert in a binary search tree iterative
	# time complexity: O(h)
	# space complexity: O(1)
	def insert_i(self,data):
		new = self.Node(data)
		if not self.root:
			self.root = new
			return
		curr = self.root
		while curr:
			prev = curr
			if data < curr.data:
				curr = curr.left
			elif data == curr.data:
				return
			else:
				curr = curr.right
		if data < prev.data:
			prev.left = new
		else:
			prev.right = new

	
	# search in a binary search tree recursive
	# time complexity: O(h)
	# space complexity: O(h)
	def search(self,node,data):
		if not node: 
			return node
		if data < node.data:
			return self.search(node.left,data)
		elif node.data == data:
			return node
		else:
			return self.search(node.right,data)
	# search in a binary search tree iterative
	# time complexity: O(h)
	# space complexity: O(1)
	def search_i(self,data):
		if not self.root:
			return root
		curr = self.root
		while curr:
			if data < curr.data:
				curr = curr.left
			elif data == curr.data:
				return curr
			else:
				curr = curr.right
		return None


	# delete from a binary search tree
	# time complexity: O(h)
	# space complexity: O(1)
	def delete(self,data):
		if not self.root:
			return
		prev = None
		curr = self.root
		while curr:
			if data < curr.data:
				prev = curr
				curr = curr.left
			elif data == curr.data:
				break
			else:
				prev = curr
				curr = curr.right
		if not curr:
			return

		if not curr.right and not curr.left:
			child = None
		elif not curr.right or not curr.left:
			child = curr.left or curr.right
		else:
			preS = curr
			successor = curr.right
			while successor.left:
				preS = successor
				successor = successor.left
			if successor == preS.left:
				preS.left = successor.right
			else:
				preS.right = successor.right
			successor.left = curr.left
			successor.right = curr.right
			child = successor

		if not prev:
			self.root = child
		else:
			if curr == prev.left:
				prev.left = child
			else:
				prev.right = child

	
	# min element in a binary tree
	# time complexity: O(h)
	# space complexity: O(1)
	def minNode(self):
		if not self.root:
			return sys.maxint
		curr = self.root
		while curr.left:
			curr = curr.left
		return curr

	# max element in a binary tree
	# time complexity: O(h)
	# space complexity: O(1)
	def maxNode(self):
		if not self.root:
			return -sys.maxint
		curr = self.root
		while curr.right:
			curr = curr.right
		return curr
		

	# check if the binary tree is a binary search tree
	# time complexity: O(n)
	# space complexity: O(h)
	def isBST(self,node):
		if not node:
			return True
		inO = self.inOrder_i(self.root)
		for i in range(1,len(inO)):
			if inO[i].data < inO[i-1].data:
				return False
		return True

	# kth min element in a binary tree
	# time complexity: O(h)
	# space complexity: O(n+w)
	def minNode_K(self,k):
		inO = self.inOrder_i(self.root)
		try:
			return inO[k-1]
		except:
			return sys.maxint

	# kth max element in a binary tree
	# time complexity: O(h)
	# space complexity: O(n+w)
	def maxNode_K(self,k):
		inO = self.inOrder_i(self.root)
		try:
			return inO[-k]
		except:
			return -sys.maxint
	

	# floor of an element in a binary search tree
	# time complexity: O(h)
	# space complexity: O(1)
	def floor(self,data):
		if not self.root:
			return root
		curr = self.root
		f = sys.maxint
		while curr:
			if data < curr.data:
				curr = curr.left
			elif data == curr.data:
				f = curr.data
				break
			else:
				f = curr.data
				curr = curr.right
		return f

	# ceil of an element in a binary search tree
	# time complexity: O(h)
	# space complexity: O(1)
	def ceil(self,data):
		if not self.root:
			return root
		curr = self.root
		c = -sys.maxint
		while curr:
			if data < curr.data:
				c = curr.data
				curr = curr.left
			elif data == curr.data:
				c = curr.data
				break
			else:
				curr = curr.right
		return c


	# inorder predecessor and successor of an element in a binary search tree
	# time complexity: O(h)
	# space complexity: O(1)
	def findPreSuc(self,data):
		if not self.root:
			return self.root,self.root
		
		pre = None
		curr = self.root
		while curr:
			if data < curr.data:
				curr = curr.left
			elif data == curr.data:
				break
			else:
				pre = curr
				curr = curr.right

		suc = None
		curr = self.root
		while curr:
			if data < curr.data:
				suc = curr
				curr = curr.left
			elif data == curr.data:
				break
			else:
				curr = curr.right
		
		return pre,suc
		

	# lowest common ancestors of two elements in a binary search tree
	# time complexity: O(h)
	# space complexity: O(1)
	def lca(self,e1,e2):
		if not self.root:
			return self.root
		if not self.search_i(e1) or not self.search_i(e2):
			return None
		
		lca = None
		curr = self.root
		while curr:
			if e1 < curr.data and e2 < curr.data:
				curr = curr.left
			elif (e1 <= curr.data and e2 >= curr.data) or (e1 >= curr.data and e2 <= curr.data):
				lca = curr
				break
			else:
				curr = curr.right
		if not curr:
			return None
		return curr
		
		
# to print a list of nodes
# time complexity: O(n)
# space complexity: O(1)
def myprint(list):
	for node in list:
		print node,
	print

# construct a binary search tree from its preorder traversal
# time complexity: O(n)
# space complexity: O(n)
def constructTree(pre):
	tree = BinarySearchTree()
	tree.root = tree.Node(pre[0])
	mystack = []
	mystack.append(tree.root)
	temp = None
	for i in range(1,len(pre)):
		while len(mystack) and pre[i] > mystack[-1].data:
			temp = mystack.pop()
		if temp:
			temp.right = tree.Node(pre[i])
			mystack.append(temp.right)
		else:
			mystack[-1].left = tree.Node(pre[i])
			mystack.append(mystack[-1].left)
	return tree



# generate a binary search tree of random elements and print
myTree = BinarySearchTree()

for i in range(15):
 	temp = random.randint(0,99)
 	myTree.insert_i(temp) 

print "Binary Search Tree"

print "Inorder Traversal:    ",
myprint(myTree.inOrder_i(myTree.root))
print "Level Order Traversal:",
myprint(myTree.levelOrder_i(myTree.root))

