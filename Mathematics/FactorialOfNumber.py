class Solution:
    #You need to complete this function
    def factorial(self,N):
        #Your code here
        if N ==0:
            return 1
        res = N  
        while N >1:
            res = res*(N-1)
            N = N-1
        return res
