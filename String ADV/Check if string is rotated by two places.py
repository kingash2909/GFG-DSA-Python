

class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here

        if len(str1) != len(str2):
            return False
        
        # Rotate str1 by exactly 2 places in both directions.
        rotated_str1_clockwise = str1[2:] + str1[:2]
        rotated_str1_anticlockwise = str1[-2:] + str1[:-2]
        
        # Check if str2 matches with either rotated version of str1.
        if str2 == rotated_str1_clockwise or str2 == rotated_str1_anticlockwise:
            return True
        else:
            return False
            