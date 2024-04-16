
class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        #code here
        set_s1 = set(s1)
        set_s2 = set(s2)
        
        # Initialize variables to store uncommon characters.
        uncommon_s1 = ""
        uncommon_s2 = ""
        
        # Iterate through each character in s1.
        for char in s1:
            # If the character is not common, add it to uncommon_s1.
            if char not in set_s2:
                uncommon_s1 += char
        
        # Iterate through each character in s2.
        for char in s2:
            # If the character is not common, add it to uncommon_s2.
            if char not in set_s1:
                uncommon_s2 += char
        
        # Concatenate uncommon characters from both strings.
        concatenated = uncommon_s1 + uncommon_s2
        
        # Return the concatenated string if it's not empty, otherwise return -1.
        if concatenated:
            return concatenated
        else:
            return -1