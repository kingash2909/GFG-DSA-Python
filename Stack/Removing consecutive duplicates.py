
class Solution:
    
    #Function to remove consecutive duplicates from given string using Stack.
    def removeConsecutiveDuplicates(self,s):
        # code here
        stack = []  # Initialize an empty stack
        # Iterate through each character in the string
        for char in s:
            # If the stack is empty or the current character is different from the top of the stack
            if not stack or char != stack[-1]:
                # Push the current character onto the stack
                stack.append(char)
        # Join the characters on the stack to form the resulting string
        return ''.join(stack)
