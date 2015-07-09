'''

Name:    Sorting Array                                      
Purpose: Sort the given array of numbers in ascending order                                       
Created by: TigerApps                                 

'''

import random
import math


#comparator
def compare_int(a,b):
    if a<=b:
        return True
    else:
        return False


# selection sort
# time complexity: O(n^2)
# space complexity: O(1)
def selection(function,list,n):
    arr = list[:]
    for i in range(n):
        small = i
        for j in range(i+1,n):
            if function(arr[j] , arr[small]):
                if function(arr[small],arr[j]): #continue if arr[j] == arr[small] for stable
                    continue;
                j , small = small , j
        arr[i] , arr[small] = arr[small] , arr[i]
    return arr

# bubble sort
# time complexity: O(n^2)
# space complexity: O(1)
def bubble(function,list,n):
    arr = list[:]
    for i in range(n):
        for j in range(n-1-i):
            if function(arr[j+1],arr[j]):
                if function(arr[j],arr[j+1]): #continue if arr[j] == arr[j+1] for stable 
                    continue;
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

# insertion sort
# time complexity: O(n^2)
# space complexity: O(1)
def insertion(function,list,n):
    arr = list[:]
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and function(temp,arr[j]) and not function(arr[j],temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp            
    return arr

# merge sort
# time complexity: O(nLog(n))
# space complexity: O(n),
def mergesort(function,list,s,e):
    arr =list[:]
    merge_h(function,arr,s,e)
    return arr

def merge_h(function,arr,s,e):
    if s == e:
        return arr
    m = (e-s)/2 + s #divide at midpoint
    merge_h(function,arr,s,m)
    merge_h(function,arr,m+1,e) #conquer the halves
    arr = merge(function,arr,s,e)
    return arr

# merge function
def merge(function,arr,s,e):
    m = (e-s)/2 + s
    left  = arr[s:m+1]
    l = 0
    right = arr[m+1:e+1]
    r = 0
    for i in range(s,e+1):  
        if l<m+1-s and r<e-m:   #while l and r in range, keep adding smalled
            if function(left[l] , right[r]):
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
def quicksort(function,list,s,e):
    arr = list[:]
    quick(function,arr,s,e)
    return arr

def quick(function,arr,s,e):
    if s>=e:
        return arr
    partition = quick_h(function,arr,s,e)
    quick(function,arr,s,partition-1)
    quick(function,arr,partition+1,e)
    return arr

# partition fucntion
def quick_h(function,arr,s,e):
    j = s
    for i in range(s,e):
        if function(arr[i] , arr[e]):
            arr[i] , arr[j] = arr[j] , arr[i]
            j += 1
    arr[j] , arr[e] = arr[e] , arr[j]
    return j

# shell sort
# time complexity: O(n^(3/2))
# space complexity: O(1)
def shell(function,list):
    arr = list[:]
    n = len(arr)
    gap = int(math.pow(2,math.floor(math.log(n,2))-1))-1 # 2^k - 1
    while gap>=1:
        for i in range(1,n):
            temp = arr[i]
            j = i - gap
            while j>=0 and function(temp,arr[j]) and not function(arr[j],temp):
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = ((gap + 1 ) / 2 ) - 1
    return arr

# heap sort
# time complexity: O(nLog(n))
# space complexity: O(1)
class heap:
    def __init__(self, function, arr):
        self.list = arr[:]
        self.n = len(arr)
        self.comparator = function

    def __str__(self):
        return ''.join(str(self.list))

    def __heapify(self,i,l):
        left = 2 * i + 1
        right = left + 1
        large = i
        if left < l and self.comparator(self.list[large] , self.list[left]):
            large = left
        if right < l and self.comparator(self.list[large] , self.list[right]):
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
        return self.list

#array of random integers
arr = []
n = 15
for i in range(n):  
    arr.append(random.randint(0,100))

print "Sorting Array"
print "Array:          ",arr
print "Sorted Array:   ",sorted(arr)
print "Selection Sort: ",selection(compare_int,arr,n)
print "Bubble Sort:    ",bubble(compare_int,arr,n)
print "Insertion Sort: ",insertion(compare_int,arr,n)
print "Merge Sort:     ",mergesort(compare_int,arr,0,n-1)
print "Quick Sort:     ",quicksort(compare_int,arr,0,n-1)
print "Shell Sort:     ",shell(compare_int,arr)
print "Heap Sort:      ",heap(compare_int,arr).heapsort()
print "Array:          ",arr
