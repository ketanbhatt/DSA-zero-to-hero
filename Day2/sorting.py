'''

Name:    Sorting                                       
Purpose: Sort the given array of numbers in ascending order                                       
Created by: TigerApps                                 

'''

import random

# selection sort
# time complexity: O(n^2)
# space complexity: O(1)
def selection(arr):
    n = len(arr)
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
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

# insertion sort
# time complexity: O(n^2)
# space complexity: O(1)
def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        temp = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[temp]:
                arr[j] , arr[temp] = arr[temp] , arr[j]
                temp = j

    return arr

# merge sort
# time complexity:
# space complexity:
def merge(arr):
    return arr

# quick sort
# time complexity:
# space complexity:
def quick(arr):
    return arr

# heap sort
# time complexity:
# space complexity:
def heap(arr):
    return arr

#array ofrandom ints
arr = []
n = 16
for i in range(n):  
    arr.append(random.randint(0,100))

l1 = arr[:]
l2 = arr[:]
l3 = arr[:]
l4 = arr[:]
l5 = arr[:]
l6 = arr[:]

print "Array:           ",arr
print "Sorted Array:    ",sorted(arr)
print "Selection Sort:  ",selection(l1)
print "Bubble Sort:     ",bubble(l2)
print "Insertion Sort:  ",insertion(l3)
print "Merge Sort:      ",merge(l4)
print "Quick Sort:      ",quick(l5)
print "Heap Sort:       ",heap(l6)

