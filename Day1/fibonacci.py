'''

Name:    Fibonacci                                       
Purpose: Print first n numbers from the Fibonacci Seqeunce                                        
Created by: TigerApps                                 

'''

class Fibonacci_Series:
    def __init__(self,n,s):
        self.length = n
        self.start = s-1
        self.series = self.fiboDP()[:]    #dp approach chosen
        
    def __str__(self):
        return ''.join(str(self.series[self.start:]))

    # iterative way  
    # time complexity: O(n) 
    # space complexity: O(n)
    def fiboIter(self):
        ans = []
        f = 0 #first
        s = 1 #second
        for i in xrange(self.length):
            ans.append(f)
            f , s = s , f + s
        return ans

    # iterative way (find nth Fibonacci element)  
    # time complexity: O(n) 
    # space complexity: O(1)
    def fiboIter_k(self):
        f = 0 #first
        s = 1 #second
        for i in xrange(self.length):
            f , s = s , f + s
        return f

    # recursive way #not recommended
    # time complexity: exponential (approx 2^n)
    # space complexity: exponential
    def fiboRec(self):
        ans_r = []        
        for i in xrange(0,self.length):
            ans_r.append(self.__fiboRec_h(i))     
        return ans_r

    # recursion helper
    def __fiboRec_h(self,n):
        if n==0:        #first
            return 0    
        elif n==1:      #second
            return 1
        else:
            return self.__fiboRec_h(n-1)+self.__fiboRec_h(n-2)

    # memoization (top-down)
    # time complexity: O(n)
    # space complexity: O(n)
    def fiboMem(self):
        ans_m = []       
        ans_m.append(0)  #first
        ans_m.append(1)  #second
        self.__fiboMem_h(ans_m,self.length-1)
        return ans_m
    
    # memoization helper
    def __fiboMem_h(self,ans_m,n):
        try:
            return ans_m[n]
        except:
            ans_m.append(self.__fiboMem_h(ans_m,n-1)+self.__fiboMem_h(ans_m,n-2))
            return ans_m[n]
    
    # dynamic programming (bottom-up)
    # time complexity: O(n)
    # space complexity: O(n)
    def fiboDP(self):
        ans_dp = []
        ans_dp.append(0)  #first
        ans_dp.append(1)  #second
        for i in xrange(2,self.length):
            ans_dp.append(ans_dp[i-1]+ans_dp[i-2])
        return ans_dp

    # print result of different approaches
    def fs_print(self):
        print "Fibonacci Series"
        print "Iterative:           ",self.fiboIter()[self.start:]
        print "Recursive:           ",self.fiboRec()[self.start:]
        print "Memoization:         ",self.fiboMem()[self.start:]
        print "Dynamic Programming: ",self.series[self.start:]


temp = "1 10"
try:
    start,end=map(int,temp.strip().split())   #for start,end
except:
    start = end = int(temp.strip())           #for nth element

fs = Fibonacci_Series(end,start)    
fs.fs_print()
#print fs 	