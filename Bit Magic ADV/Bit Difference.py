
class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here

        # XOR A and B to find different bits
        xor_result = a ^ b
        
        # Count the number of set bits in xor_result
        count = 0
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        
        return count