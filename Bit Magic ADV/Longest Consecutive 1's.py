
class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        # Convert integer to binary string
        binary_str = bin(N)[2:]
        
        # Initialize variables to track consecutive ones
        max_count = 0
        current_count = 0
        
        # Iterate through the binary string
        for bit in binary_str:
            if bit == '1':
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        
        return max_count