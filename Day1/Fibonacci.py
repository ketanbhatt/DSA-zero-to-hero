'''

Name:    Fibonacci                                       
Purpose: Print first n numbers from the Fibonacci Seqeunce                                        
Created by: TigerApps                                 

'''

class Fibonacci_Series:
    def __init__(self,n):
        self.length = n

    # iterative way , time complexity: O(n), space complexity: O(1)
    def Fibonacci_i(self):
        ans = ""
        f = 0 #first
        s = 1 #second
        for i in xrange(self.length):
            ans += str(f) + " "
            f , s = s , f + s
        return ans[:-1]   #to delete the last space

    # recursive way #not recommended
    def Fibonacci_r(self):
        ans_r = ""        #basic recursion, time complexity: exponential
        for i in xrange(0,self.length):
            ans_r += str(self.__Fibonacci_r_h(i)) + " "        
        return ans_r[:-1]

    # basic recursion
    def __Fibonacci_r_h(self,n):
        if n==0:        #first
            return 0    
        elif n==1:      #second
            return 1
        else:
            return self.__Fibonacci_r_h(n-1)+self.__Fibonacci_r_h(n-2)

    # recursive memoized way
    def Fibonacci_m(self):
        ans_m = ""        #recursion wtih memoization, time complexity: O(n), space complexity: O(n)
        mylist = []
        mylist.append(0)  #first
        mylist.append(1)  #second
        for i in xrange(0,self.length):
            ans_m += str(self.__Fibonacci_m_h(mylist,i)) + " "
        return ans_m[:-1]

    # memoization
    def __Fibonacci_m_h(self,mylist,n):
        try:
            return mylist[n]
        except:
            mylist.append(mylist[n-1] + mylist[n-2])
            return mylist[n]
    
    def __str__(self):
        return self.Fibonacci_i() + "\n" + self.Fibonacci_r() + "\n" + self.Fibonacci_m()

    
n=input("Enter n: ")
print Fibonacci_Series(n)    
