class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        # code here
        # Initialize an empty stack
        stack = []
        # Iterate through each character in the string
        for char in s:
            # If the stack is not empty and the current character is the same as the top of the stack
            if stack and char == stack[-1]:
                # Remove the character from the stack (remove the duplicate pair)
                stack.pop()
            else:
                # Otherwise, push the character onto the stack
                stack.append(char)
        # Join the remaining characters on the stack to form the resulting string
        return ''.join(stack)