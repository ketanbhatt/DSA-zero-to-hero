'''

Name:    Sorting                                       
Purpose: Sort the given array of numbers in ascending order                                       
Created by: TigerApps                                 

'''

import random

# selection sort
# time complexity:
# space complexity:
def selection(arr):
    return arr

# bubble sort
# time complexity:
# space complexity:
def bubble(arr):
    return arr

# insertion sort
# time complexity:
# space complexity:
def insertion(arr):
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


arr = []
n = 10
for i in range(n):  #array of random ints
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

