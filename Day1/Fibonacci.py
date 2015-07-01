'''

Name:    Fibonacci                                       
Purpose: Print first n numbers from the Fibonacci Seqeunce                                        
Created by: TigerApps                                 

'''


# iterative way , time complexity: O(n), space complexity: O(1)
def Fibonacci(n):
    ans = ""
    f = 0 #first
    s = 1 #second
    for i in xrange(n):
        ans += str(f) + " "
        f , s = s , f + s
    return ans[:-1]   #to delete the last space

# recursive way
def Fibonacci_r(n):
    ans_r = ""        # basic recursion, time complexity: exponential
    ans_m = ""        # recursion wtih memoization, time complexity: O(n), space complexity: O(n)
    mylist = []
    mylist.append(0)  #first
    mylist.append(1)  #second

    for i in xrange(0,n):
        #ans_r += str(Fibonacci_r_h(i)) + " "        #not recommended
        ans_m += str(Fibonacci_r_m(mylist,i)) + " "
    return ans_r[:-1] + "\n" + ans_m[:-1]

# basic recurseion
def Fibonacci_r_h(n):
    if n==0:        #first
        return 0    
    elif n==1:      #second
        return 1
    else:
        return Fibonacci_r_h(n-1)+Fibonacci_r_h(n-2)

# memoization
def Fibonacci_r_m(mylist,n):
    try:
        return mylist[n]
    except:
        mylist.append(mylist[n-1] + mylist[n-2])
        return mylist[n]
    
n=input("Enter n: ")
print Fibonacci(n)
print Fibonacci_r(n)
    
