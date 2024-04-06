class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        # Shift odd bits to the left and even bits to the right
        even_bits = n & 0xAAAAAAAA  # Mask to extract even bits
        odd_bits = n & 0x55555555   # Mask to extract odd bits
        even_bits >>= 1
        odd_bits <<= 1
        
        # Combine even and odd bits
        result = even_bits | odd_bits
        
        return result
