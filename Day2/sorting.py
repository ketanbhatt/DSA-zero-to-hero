'''

Name:    Sorting                                       
Purpose: Sort the given array of numbers in ascending order                                       
Created by: TigerApps                                 

'''

import random
import math

# selection sort
# time complexity: O(n^2)
# space complexity: O(1)
def selection(arr,n):
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if arr[j] < arr[small]:
                j , small = small , j
        arr[i] , arr[small] = arr[small] , arr[i]
    return arr

# bubble sort
# time complexity: O(n^2)
# space complexity: O(1)
def bubble(arr,n):
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

# insertion sort
# time complexity: O(n^2)
# space complexity: O(1)
def insertion(arr,n):
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp            
    return arr

# merge sort
# time complexity: O(nLog(n))
# space complexity: O(n)
def merge(arr,s,e):
    if s == e:
        return arr
    m = (e-s)/2 + s #divide at midpoint
    merge(arr,s,m)
    merge(arr,m+1,e) #conquer the halves
    arr = merge_h(arr,s,e)
    return arr

# merge function
def merge_h(arr,s,e):
    m = (e-s)/2 + s
    left  = arr[s:m+1]
    l = 0
    right = arr[m+1:e+1]
    r = 0
    for i in range(s,e+1):  
        if l<m+1-s and r<e-m:   #while l and r in range, keep adding smalled
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
        elif l>=m+1-s:      #l out of range, add right
            arr[i] = right[r]
            r += 1  
        else:               #r out of range, add left
            arr[i] = left[l]
            l += 1
    return arr      

# quick sort
# time complexity: O(nLog(n))
# space complexity: O(Log(n))
def quick(arr,s,e):
    if s>=e:
        return arr
    partition = quick_h(arr,s,e)
    quick(arr,s,partition-1)
    quick(arr,partition+1,e)
    return arr

# partition fucntion
def quick_h(arr,s,e):
    j = s
    for i in range(s,e):
        if arr[i]<=arr[e]:
            arr[i] , arr[j] = arr[j] , arr[i]
            j += 1
    arr[j] , arr[e] = arr[e] , arr[j]
    return j

# heap sort
# time complexity:
# space complexity:
def heap(arr):
    return arr

# shell sort
# time complexity: O(n^(3/2))
# space complexity: O(1)
def shell(arr):
    n = len(arr)
    gap = int(math.pow(2,math.floor(math.log(n,2))-1))-1 # 2^k - 1
    while gap>=1:
        for i in range(1,n):
            temp = arr[i]
            j = i - gap
            while j>=0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = ((gap + 1 ) / 2 ) - 1
    return arr

# heap sort
# time complexity: O(nLog(n))
# space complexity: O(1)
class heap:
	def __init__(self,arr):
		self.list = arr[:]
		self.n = len(arr)
		self.heapsort()	

	def __str__(self):
		return ''.join(str(self.list))

	def __heapify(self,i,l):
		left = 2 * i + 1
		right = left + 1
		large = i
		if left < l and self.list[left] > self.list[large]:
			large = left
		if right < l and self.list[right] > self.list[large]:
			large = right
		self.list[i] , self.list[large] = self.list[large] , self.list[i]
		if large != i:
			self.__heapify(large,l)

	def heapsort(self):
		for i in range(self.n/2,-1,-1):
			self.__heapify(i,self.n)
		for i in range(self.n):
			self.list[n-i-1] , self.list[0] = self.list[0] , self.list[n-i-1]
			self.__heapify(0,n-i-1)


#array ofrandom ints
arr = []
n = 15
for i in range(n):  
    arr.append(random.randint(0,100))

l1 = arr[:]
l2 = arr[:]
l3 = arr[:]
l4 = arr[:]
l5 = arr[:]
l6 = arr[:]
l7 = arr[:]

print "Array:          ",arr
print "Sorted Array:   ",sorted(arr)
print "Selection Sort: ",selection(l1,n)
print "Bubble Sort:    ",bubble(l2,n)
print "Insertion Sort: ",insertion(l3,n)
print "Merge Sort:     ",merge(l4,0,n-1)
print "Quick Sort:     ",quick(l5,0,n-1)
print "Shell Sort:     ",shell(l6)
print "Heap Sort:      ",heap(l7)

