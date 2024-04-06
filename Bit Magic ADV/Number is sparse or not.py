
class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 

        # Convert N to its binary representation
        binary = bin(n)[2:]
        
        # Check if there are any consecutive set bits
        for i in range(len(binary) - 1):
            if binary[i] == '1' and binary[i + 1] == '1':
                return False
        
        # If no consecutive set bits found, return True
        return True
        
