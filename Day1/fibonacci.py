'''

Name:    Fibonacci                                       
Purpose: Print first n numbers from the Fibonacci Seqeunce                                        
Created by: TigerApps                                 

'''

class Fibonacci_Series:
    def __init__(self,n,s):
        self.length = n
        self.start = s-1
        self.series = self.Fibonacci_dp()[:]    #dp approach chosen
        
    def __str__(self):
        return ''.join(str(self.series[self.start:]))

    # iterative way  
    # time complexity: O(n) 
    # space complexity: O(n)
    def Fibonacci_i_s(self):
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
    def Fibonacci_i(self):
        f = 0 #first
        s = 1 #second
        for i in xrange(self.length):
            f , s = s , f + s
        return f

    # recursive way #not recommended
    # time complexity: exponential (approx 2^n)
    # space complexity: exponential
    def Fibonacci_r(self):
        ans_r = []        
        for i in xrange(0,self.length):
            ans_r.append(self.__Fibonacci_r_h(i))     
        return ans_r

    # recursion helper
    def __Fibonacci_r_h(self,n):
        if n==0:        #first
            return 0    
        elif n==1:      #second
            return 1
        else:
            return self.__Fibonacci_r_h(n-1)+self.__Fibonacci_r_h(n-2)

    # memoization (top-down)
    # time complexity: O(n)
    # space complexity: O(n)
    def Fibonacci_r_m(self):
        ans_r_m = []       
        ans_r_m.append(0)  #first
        ans_r_m.append(1)  #second
        self.__Fibonacci_r_m_h(ans_r_m,self.length-1)
        return ans_r_m
    
    # memoization helper
    def __Fibonacci_r_m_h(self,ans_r_m,n):
        try:
            return ans_r_m[n]
        except:
            ans_r_m.append(self.__Fibonacci_r_m_h(ans_r_m,n-1)+self.__Fibonacci_r_m_h(ans_r_m,n-2))
            return ans_r_m[n]
    
    # dynamic programming (bottom-up)
    # time complexity: O(n)
    # space complexity: O(n)
    def Fibonacci_dp(self):
        ans_dp = []
        ans_dp.append(0)  #first
        ans_dp.append(1)  #second
        for i in xrange(2,self.length):
            ans_dp.append(ans_dp[i-1]+ans_dp[i-2])
        return ans_dp

    # print result of different approaches
    def fs_print(self):
        print self.Fibonacci_i_s()[self.start:]
        print self.Fibonacci_r()[self.start:]
        print self.Fibonacci_r_m()[self.start:]
        print self.series[self.start:]


temp = raw_input("Enter: ")
try:
    start,end=map(int,temp.strip().split())   #for start,end
except:
    start = end = int(temp.strip())           #for nth element

fs = Fibonacci_Series(end,start)    
fs.fs_print()
#print fs 	