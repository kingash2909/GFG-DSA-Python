#Back-end complete function Template for Python 3

class Solution:
    
    #Function to print the maximum contiguous subarray sum ending at each 
    #position in the array and return the overall maximum.
    def maximumSum(self,a,n):
        
        curr_sum = 0
        max_sum = float('-inf')
        max_ending_here = [0] * n
        
        for i in range(n):
            curr_sum = max(a[i], curr_sum + a[i])
            max_ending_here[i] = curr_sum
            max_sum = max(max_sum, curr_sum)
        
        for num in max_ending_here:
            print(num, end=" ")
        print()  

        return max_sum
