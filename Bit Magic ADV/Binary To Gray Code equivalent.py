
class Solution:
    ##Complete this fcuntion
    # Function to find the n code of given number n
    def greyConverter(self,n):
        ##Your code here
        # Right-shift n by 1 bit
        gray = n >> 1
        
        # XOR n and gray to get the Gray code representation
        gray ^= n
        
        return gray
