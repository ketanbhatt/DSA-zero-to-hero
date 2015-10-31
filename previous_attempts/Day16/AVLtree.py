'''

Name:    AVL Tree                                
Purpose: Various operations on a AVL tree                                      
Created by: TigerApps                                 

'''

import random
import sys
    

# AVLtree object
class AVLtree:
    def __init__(self):
        self.root = None

    # Node object
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1

        def __str__(self):
            return str(self.data)   

    # inorder traversal of the binary tree recursive
    # time complexity: O(n)
    # space complexity: O(Log(n))
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

    # insert in a avl tree recursive
    # time complexity: O(Log(n))
    # space complexity: O(Log(n))
    def insert(self,node,data):
        if not node:
            return self.Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)

        node.height = max(self.__height(node.left),self.__height(node.right))

        bal = self.__getBal(node)
        if bal > 1 and data < node.left.data:
            return rightRotate(node)
        if bal < -1 and data > node.right.data:
            return leftRotate(node)
        if bal > 1 and data > node.left.data:
            node.left =  leftRotate(node.left)
            return rightRotate(node)
        if bal < -1 and data < node.right.data:
            node.right = rightRotate(node.right);
            return leftRotate(node)
        return node

    def __height(self,node):
        if not node:
            return 0
        return node.height

    def __getBal(self,node):
        if not node:
            return
        return self.__height(node.left)-self.__height(node.right)

    def __rightRotate(self,node):
        temp1 = node.left
        temp2 = temp1.right

        temp1.right = node
        node.left = temp2

        node.height = max(height(node.left), height(node.right))+1
        temp1.height = max(height(temp1.left), height(temp1.right))+1

        return temp1


    def __leftRotate(self,node):
        temp1 = node.right
        temp2 = temp1.left

        temp1.left = node
        node.right = temp2

        node.height = max(height(node.left), height(node.right))+1
        temp1.height = max(height(temp1.left), height(temp1.right))+1

        return temp1
    
    # search in a binary search tree recursive
    # time complexity: O(Log(n))
    # space complexity: O(Log(n))
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
    # time complexity: O(Log(n))
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


    # delete from a avl tree
    # time complexity: O(Log(n))
    # space complexity: O(1)
    def delete(self,node,data):
        if not node:
            return node


        if data < node.data:
            node.left = self.delete(node.left, data)
 
        elif data > node.data:
            node.right = self.delete(node.right, data)
 
        else:
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
     
                if not temp:
                    temp = node
                    node = None
                else:
                    node = temp
        
            else:
                temp = self.__minValueNode(node.right)
                node.data = temp.data;
                node.right = deleteNode(node.right, temp.data)
        
        if not node:
          return node
     
        node.height = max(self.__height(node.left),self.__height(node.right))

        bal = self.__getBal(node)
        if bal > 1 and data < node.left.data:
            return rightRotate(node)
        if bal < -1 and data > node.right.data:
            return leftRotate(node)
        if bal > 1 and data > node.left.data:
            node.left =  leftRotate(node.left)
            return rightRotate(node)
        if bal < -1 and data < node.right.data:
            node.right = rightRotate(node.right);
            return leftRotate(node)
        return node

    def __minValueNode(self,node):
        curr = node
 
        while curr.left:
            curr = curr.left
 
        return curr

    
        
# to print a list of nodes
# time complexity: O(n)
# space complexity: O(1)
def myprint(list):
    for node in list:
        print node,
    print


# generate a avl tree of random elements and print
myTree = AVLtree()

for i in range(15):
    temp = random.randint(0,99)
    myTree.root = myTree.insert(myTree.root,temp) 

print "AVL Tree"

print "Inorder Traversal:    ",
myprint(myTree.inOrder_i(myTree.root))
print "Level Order Traversal:",
myprint(myTree.levelOrder_i(myTree.root))

myTree.root = myTree.delete(myTree.root,temp)

print "Inorder Traversal:    ",
myprint(myTree.inOrder_i(myTree.root))
print "Level Order Traversal:",
myprint(myTree.levelOrder_i(myTree.root))

