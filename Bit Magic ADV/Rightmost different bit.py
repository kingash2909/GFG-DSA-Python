
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        # Perform XOR operation between M and N
        xor_result = m ^ n
        
        # If M and N are equal, return -1
        if xor_result == 0:
            return -1
        
        # Find the position of the rightmost set bit
        position = 1
        while xor_result & 1 == 0:
            xor_result >>= 1
            position += 1
        
        return position