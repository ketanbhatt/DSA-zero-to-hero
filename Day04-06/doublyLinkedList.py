'''

Name:    Linked List                                
Purpose: Various operations on double linked list                                       
Created by: TigerApps                                 

'''

import random

# Doubly LinkedList object
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Node object
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None

        def __str__(self):
            return str(self.data)

    # insert in a sorted list
    # time complexity: O(n)
    # space complexity: O(1)
    def insert_sorted(self,data,comparator):
        new = self.Node(data)
        if not self.head:
            self.head = new
            self.tail = new
            return
        elif comparator(data,self.head.data):
            new.next = self.head
            self.head.prev = new
            self.head = new
            return

        curr = self.head
        while curr.next and comparator(curr.next.data,data):
            curr = curr.next
        if not curr.next:
            new.prev = curr
            curr.next = new
            self.tail = new
            return
        else:
            new.prev = curr
            new.next = curr.next
            curr.next.prev = new
            curr.next = new
            return
            
    # print the linked list
    # time complexity: O(n)
    # space complexity: O(1)
    def printList(self):
        curr = self.head
        while curr:
            print curr,
            curr = curr.next
        print ""

    # print the linked list in reverse
    # time complexity: O(n)
    # space complexity: O(1)
    def printListReverse(self):
        curr = self.tail
        while curr:
            print curr,
            curr = curr.prev
        print ""

    # reverse the doubly linked list
    # time complexity: O(n)
    # space complexity: O(1)
    def reverse(self):
        if not self.head:
            return
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.tail = self.head
        self.head = prev


# comparator
def compare_int(a,b):
    return a<=b

# generate a sorted linked of random elements and print it
print "\nDoubly Linked List: "
myList = DoublyLinkedList()
n = 15

for i in range(n):  
    temp = random.randint(0,100)
    myList.insert_sorted(temp,compare_int)

myList.printList()
myList.printListReverse()


# Non Flat LinkedList object
class NFLinkedList:
    def __init__(self):
        self.head = None
        
    # Node object
    class Node:
        def __init__(self,data):
            self.data = data
            self.down = None    #main
            self.right = None   #side
            
        def __str__(self):
            return str(self.data)

    # push new element at next pointer in sorted way of main list
    # time complexity: O(n)
    # space complexity: O(1)
    def push(self,node,data):
        new = self.Node(data)
        new.down = node
        return new

    # print the linked list
    # time complexity: O(n)
    # space complexity: O(1)
    def printlist(self,node):
        curr = node
        while curr:
            print curr,
            curr = curr.down
        print ""

    # flatten the linked list
    # time complexity: O(n)
    # space complexity: O(1)
    def flatten(self,node):
        if not node or not node.right:
            return node
        else:
            return self.merge(node,self.flatten(node.right))

    # merge 2 list in a sorted way
    def merge(self,node1,node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.data < node2.data:
            result = node1 
            result.down = self.merge(node1.down,node2)
        else:
            result = node2
            result.down = self.merge(node1,node2.down)
        return result

# generate a non flat list
print "\nNon Flat Linked List: "
myNFList = NFLinkedList()

# Let us create the following linked list
#       5 -> 10 -> 19 -> 28
#       |    |     |     |
#       V    V     V     V
#       7    20    22    35
#       |          |     |
#       V          V     V
#       8          50    40
#       |                |
#       V                V
#       30               45


myNFList.head = myNFList.push( myNFList.head, 30 )
myNFList.head = myNFList.push( myNFList.head, 8 )
myNFList.head = myNFList.push( myNFList.head, 7 )
myNFList.head = myNFList.push( myNFList.head, 5 )

myNFList.head.right = myNFList.push( myNFList.head.right, 20 )
myNFList.head.right = myNFList.push( myNFList.head.right, 10 )

myNFList.head.right.right = myNFList.push( myNFList.head.right.right, 50 )
myNFList.head.right.right = myNFList.push( myNFList.head.right.right, 22 )
myNFList.head.right.right = myNFList.push( myNFList.head.right.right, 19 )

myNFList.head.right.right.right = myNFList.push( myNFList.head.right.right.right, 45 )
myNFList.head.right.right.right = myNFList.push( myNFList.head.right.right.right, 40 )
myNFList.head.right.right.right = myNFList.push( myNFList.head.right.right.right, 35 )
myNFList.head.right.right.right = myNFList.push( myNFList.head.right.right.right, 28 )

# print to check
myNFList.printlist(myNFList.head)
myNFList.printlist(myNFList.head.right)
myNFList.printlist(myNFList.head.right.right)
myNFList.printlist(myNFList.head.right.right.right)


# flattening
myNFList.head = myNFList.flatten(myNFList.head)
print "Flattened:",
myNFList.printlist(myNFList.head)