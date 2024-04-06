
class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        mask = n >> 1
        while mask != 0:
            n ^= mask
            mask >>= 1
        return n