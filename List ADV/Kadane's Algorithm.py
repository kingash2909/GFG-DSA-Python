
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        if N == 0:
            return 0
        
        max_sum = arr[0]
        curr_sum = arr[0]
        
        for i in range(1, N):
            curr_sum = max(arr[i], curr_sum + arr[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
