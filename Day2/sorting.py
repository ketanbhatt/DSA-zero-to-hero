'''

Name:    Sorting                                       
Purpose: Sort the given array of numbers in ascending order                                       
Created by: TigerApps                                 

'''

import random

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
        temp = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[temp]:
                arr[j] , arr[temp] = arr[temp] , arr[j]
                temp = j

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
# time complexity:
# space complexity:
def quick(arr,s,e):
    return arr

# heap sort
# time complexity:
# space complexity:
def heap(arr):
    return arr

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

print "Array:           ",arr
print "Sorted Array:    ",sorted(arr)
print "Selection Sort:  ",selection(l1,n)
print "Bubble Sort:     ",bubble(l2,n)
print "Insertion Sort:  ",insertion(l3,n)
print "Merge Sort:      ",merge(l4,0,n-1)
print "Quick Sort:      ",quick(l5,0,n-1)
print "Heap Sort:       ",heap(l6)

