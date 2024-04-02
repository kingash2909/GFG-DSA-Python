class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        
        if N % 2 == 0:
            median = (A[N//2 - 1] + A[N//2]) // 2
        else:
            median = A[N//2]
        return median
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        ##Your code here
        mean = sum(A) // N
        return mean