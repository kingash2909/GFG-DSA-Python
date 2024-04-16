
class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        char_freq = {}
        
        # Iterate through the string to count the frequency of each character.
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Initialize variables to store the maximum frequency and character.
        max_freq = float('-inf')
        max_char = ''
        
        # Iterate through the dictionary to find the character with the maximum frequency.
        for char, freq in char_freq.items():
            if freq > max_freq or (freq == max_freq and char < max_char):
                max_freq = freq
                max_char = char
        
        # Return the character with the maximum frequency.
        return max_char