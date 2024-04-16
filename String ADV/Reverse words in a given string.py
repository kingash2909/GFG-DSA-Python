
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words = S.split('.')
        
        # Reverse the list of words.
        reversed_words = words[::-1]
        
        # Join the reversed words into a string with dots as separators.
        reversed_string = '.'.join(reversed_words)
        
        # Return the reversed string.
        return reversed_string
