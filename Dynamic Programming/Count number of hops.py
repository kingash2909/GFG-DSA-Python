
class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        
        # code here
        mod = 1000000007
        #base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        
        
        #initializing base values.    
        a = 1
        b = 2
        c = 4
        
        for i in range (4, n+1):
            temp = (a + b + c) % mod
            #updating a as b and b as c and c as temp (sum of a, b and c).
            a = b 
            b = c
            c = temp
         
        #returning the result.   
        return c
        