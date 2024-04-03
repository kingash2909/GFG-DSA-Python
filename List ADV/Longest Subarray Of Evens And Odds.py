
class Solution:
    #Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self,arr,n):
        
        #returns: the maximum length
        
        #code here

        max_length = 1  # Minimum possible length of alternating subarray
        curr_length = 1  # Current length of alternating subarray
    
        # Iterate through the array starting from the second element
        for i in range(1, n):
            # If the current element and the previous element have different parity
            if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
                curr_length += 1  # Increment current length
                max_length = max(max_length, curr_length)  # Update maximum length
            else:
                curr_length = 1  # Reset current length if the alternating pattern breaks
    
        return max_length