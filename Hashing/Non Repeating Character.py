
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        # Create a dictionary to store the frequency of each character
        frequency_dict = {}
        
        # Count the frequency of each character in the string
        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        # Iterate through the string and find the first character with a frequency of 1
        for char in s:
            if frequency_dict[char] == 1:
                return char
        
        # If no non-repeating character is found, return '$'
        return '$'
