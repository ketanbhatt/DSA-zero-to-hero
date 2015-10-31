'''

Name:    Linked List                                
Purpose: Various operations on a singly linked list                                       
Created by: TigerApps                                 

'''

import random

# LinkedList object
class LinkedList:
	def __init__(self):
		self.head = None

	# Node object
	class Node:
		def __init__(self,data):
			self.data = data
			self.next = None

		def __str__(self):
			return str(self.data)	

	# insert at head
	# time complexity: O(1)
	# space complexity: O(1)
	def insert_head(self,data):
		new = self.Node(data)
		new.next = self.head
		self.head = new

	# insert at tail
	# time complexity: O(n)
	# space complexity: O(1)
	def insert_tail(self,data):
		new = self.Node(data)
		if self.head:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = new
		else:
			self.head = new

	# insert at position k
	# time complexity: O(k)
	# space complexity: O(1)
	def insert_k(self,data,position):
		new = self.Node(data)
		curr = self.head

		if position == 0:
			new.next = self.head
			self.head = new

		position -= 1
		while curr.next and position:
			curr = curr.next
			position -= 1

		if position:
			return
		
		new.next = curr.next
		curr.next = new

	# insert in a sorted list
	# time complexity: O(n)
	# space complexity: O(1)
	def insert_sorted(self,data,comparator):
		new = self.Node(data)
		if not self.head or comparator(data,self.head.data):
			new.next = self.head
			self.head = new
		
		elif not self.head.next and not comparator(data,self.head.data):
			self.head.next = new

		else:
			curr = self.head
			while curr.next and comparator(curr.next.data,data):
				curr = curr.next
			new.next = curr.next
			curr.next = new

	# print the linked list
	# time complexity: O(n)
	# space complexity: O(1)
	def printList(self):
		curr = self.head
		while curr:
			print curr,
			curr = curr.next
		print ""
		
	# print kth node from last
	# time complexity: O(n)
	# space complexity: O(1)
	def print_k(self,position):
		if not self.head:
			return
		curr = self.head
		curr_fast = self.head
		while curr_fast and position:
			curr_fast = curr_fast.next
			position -= 1
		if not curr_fast:
			return None
		while curr_fast.next:
			curr = curr.next
			curr_fast = curr_fast.next
		return curr

	# print the linked list in reverse order
	# time complexity: O(n)
	# space complexity: O(1)
	def printListReverse(self,curr):
		if not curr:
			return
		self.printlistreverse(curr.next)	
		print curr,

	# delete node with given data
	# time complexity: O(n)
	# space complexity: O(1)
	def delete(self,data):
		if self.head.data == data:
			self.head = self.head.next
			return

		curr = self.head
		
		while curr.next and curr.next.data != data:
				curr = curr.next
		if curr:
			curr.next = curr.next.next


	# delete the node at position k
	# time complexity: O(k)
	# space complexity: O(1)
	def delete_k(self,position):
		if position == 0:
			self.head = self.head.next
			return
		curr = self.head
		position -= 1
		while curr.next.next and position:
			curr = curr.next
			position -= 1
		if position:
			return
		curr.next = curr.next.next


	# reverse the linked list
	# time complexity: O(n)
	# space complexity: O(1)
	def reverse(self):
		if not self.head:
			return
		curr = self.head
		prev  = None
		while curr:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev

	# pairwise swap the nodes of a linked list
	# time complexity: O(n)
	# space complexity: O(1)
	def pairWiseSwap(self):
		if not self.head:
			return
		curr = self.head
		prev = curr
		self.head = curr.next
		while curr and curr.next:
			next = curr.next
			prev.next = next
			curr.next = next.next
			next.next = curr
			prev = curr
			curr = curr.next

	# delete duplicate nodes in a sorted linked list
	# time complexity: O(n)
	# space complexity: O(1)
	def RemoveDuplicatesSorted(self):
		if not self.head:
			return
		curr = self.head
		while curr and curr.next:
			if curr.next.data == curr.data:
				curr.next=curr.next.next
			else:
				curr = curr.next

	# delete duplicate nodes in a unsorted linked list
	# time complexity: O(n)  hashmap access time: O(1)
	# space complexity: O(n)
	def RemoveDuplicates(self):
		if not self.head:
			return
		myhash = []
		curr = self.head
		prev = None
		while curr:
			if curr.data not in myhash:
				myhash.append(curr.data)
				prev = curr
			else:
				prev.next = curr.next
				curr = curr.next

	# detect if the linked list has cycle
	# time complexity: O(n)
	# space complexity: O(1)
	def HasCycle(self):
		if not self.head:
			return
		curr = self.head
		curr_fast = self.head.next
		while curr_fast:
			if curr_fast == curr:
				return True
			curr = curr.next
			curr_fast = curr_fast.next.next
		return False


	# rotate the linked list counter-clockwise by k nodes
	# time complexity: O(n)
	# space complexity: O(1)
	def Rotate(self,k):
		if not k:
			return
		curr = self.head
		prev = None
		while curr and k:
			prev = curr
			curr = curr.next
			k -= 1
		if curr:
			head = curr
			while curr.next:
				curr = curr.next
			curr.next = self.head
			self.head = head
			prev.next = None

	# check if the linked list is a palindrome
	# time complexity: O(n)
	# space complexity: O(1)
	def isPalindrome(self):
		if not self.head:
			return
		slow = self.head
		fast = slow

		while fast.next and fast.next.next:	#saves mid in slow
			fast = fast.next.next
			slow = slow.next

		second = slow.next	#second half
		first = self.head 	#first half
		self.head = second
		self.reverse() 		#reverse second half
		curr = first
		second = self.head  #reverse second half
		while second:
			if second.data != curr.data:
				self.reverse()
				self.head = first
				return False
			second = second.next
			curr = curr.next
		self.reverse()
		self.head = first
		return True

# comparator
def compare_int(a,b):
	return a<=b

# compare two linked lists
# time complexity: O(n)
# space complexity: O(1)
def CompareLists(list1,list2):
	curr1 = list1.head
	curr2 = list2.head
	while curr1 and curr2 and curr1.data == curr2.data:
		curr1 = curr1.next
		curr2 = curr2.next
	if not curr1 and not curr2:
		return True
	else:
		return False

# merge sort a linked list
# time complexity: O(nLogn)
# space complexity: O(n+m)
def MergeSort(first,comparator):
	if not first.head or not first.head.next:
		return first
	firstTail = Mid(first.head)
	second = LinkedList()
	second.head =  firstTail.next 
	firstTail.next = None
	
	first = MergeSort(first,comparator)
	second = MergeSort(second,comparator)
	
	return Merge(first,second,comparator)
	
def Mid(node):
	if not node or not node.next:
		return node
	slow = node
	fast = slow
	while fast.next and fast.next.next:
		fast = fast.next.next
		slow = slow.next
	return slow

# merge two sorted linked lists
# time complexity: O(n)
# space complexity: O(n+m)
def Merge(list1,list2,comparator):
	curr1 = list1.head
	curr2 = list2.head
	mylist = LinkedList()
	mylist.insert_head(0)
	curr = mylist.head
	while curr1 and curr2:
		if comparator(curr1.data,curr2.data):
			curr.next = curr1
			curr = curr.next
			curr1 = curr1.next
		else:
			curr.next = curr2
			curr = curr.next
			curr2 = curr2.next
	if curr1:
			curr.next = curr1
	elif curr2:
			curr.next = curr2
	mylist.delete_k(0)
	return mylist


# quick sort a linked list
# time complexity: O(nLogn)
# space complexity: O(1)
def QuickSort(first,comparator):
	end = first
	while end.next:
		end = end.next
	return QuickSort_h(first,end,comparator)


def QuickSort_h(first,end,comparator):
	if not first or not first.next:
		return first
	first,end,pivot = Partition(first,end,comparator)
	
	if first != pivot:
		curr = first
		while curr.next != pivot:
			curr = curr.next
		curr.next = None
		first = QuickSort_h(first,curr,comparator)
		curr = first
		while curr.next:
			curr = curr.next
		curr.next = pivot
	
	second = QuickSort_h(pivot.next,end,comparator)
	pivot.next = second
	return first

def Partition(first,end,comparator):
	tail = pivot = end
	curr = first
	prev = None
	newhead = None
	while curr != pivot:
		temp = curr.next
		if comparator(curr.data,pivot.data):
			if not newhead:
				newhead = curr
			prev = curr
			curr = curr.next
		else:
			if prev:
				prev.next = curr.next
			curr.next = None
			tail.next = curr
			tail = tail.next
			curr = temp

	if not newhead:
		newhead = pivot
	return newhead,tail,pivot



# merge point of 2 linked lists
# time complexity: O(n)
# space complexity: O(1)
def FindMergeNode(list1,list2):
	len1 = 0
	curr1 = list1.head
	while curr1:
		len1 += 1
		curr1 = curr1.next
	len2 = 0
	curr2 = list2.head
	while curr2:
		len2 += 1
		curr2 = curr2.next
	curr1 = list1.head
	curr2 = list2.head

	if len1>len2:
		temp = len1 - len2
		while temp:
			curr1 = curr1.next
			temp -= 1
	else:
		temp = len2 - len1
		while temp:
			curr2 = curr2.next
			temp -= 1

	while curr1 and curr2:
		if curr1 == curr2:
			return curr1
		curr1 = curr1.next
		curr2 = curr2.next
	return None

# add two numbers represented by linked lists
# time complexity: O(n+m)
# space complexity: O(1)
def add(list1,list2):
	list1.reverse()
	list2.reverse()

	result = LinkedList()

	curr1 = list1.head
	curr2 = list2.head

	carry = 0
	while curr1 and curr2:
		sum = curr1.data + curr2.data +carry
		carry = sum/10
		sum %= 10
		result.insert_head(sum)
		curr1 = curr1.next
		curr2 = curr2.next

	if curr1:
		while curr1:
			sum = curr1.data + carry
			carr = sum/10
			sum %= 10
			result.insert_head(sum)
			curr1 = curr1.next
	elif curr2:
		while curr2:
			sum = curr2.data + carry
			carr = sum/10
			sum %= 10
			result.insert_head(sum)
			curr2 = curr2.next
	if carry:
		result.insert_head(carry)
	list1.reverse()
	list2.reverse()
	return result

# generate a sorted linked of random elements and print it
myList = LinkedList()
n = 16
for i in range(n):  
	temp = random.randint(0,100)
 	myList.insert_tail(temp)

print "Linked List:" 
myList.printList()

myList.head = QuickSort(myList.head,compare_int)
print "mylist:",
myList.printList()