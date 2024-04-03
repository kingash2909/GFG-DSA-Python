
class Solution:
    def countVowels(self,s):
        #code here
        
        # Define a set to store vowels
        vowels = set('aeiou')
    
        # Initialize a variable to count vowels
        count = 0
    
        # Iterate through the string and count vowels
        for char in s:
            if char in vowels:
                count += 1
    
        return count