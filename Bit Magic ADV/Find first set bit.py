
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        
        # Initialize position to 1
        position = 1
        
        # Check each bit from right to left
        while n > 0:
            # Check if rightmost bit is set
            if n & 1 == 1:
                return position
            # Move to the next bit
            n >>= 1
            position += 1
        
        # If no set bit found, return 0
        return 0
        