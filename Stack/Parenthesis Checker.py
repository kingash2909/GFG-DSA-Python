
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        # Initialize an empty stack
        stack = []
        # Define a mapping of opening to closing symbols
        mapping = {')': '(', '}': '{', ']': '['}
        # Iterate through each character in the expression
        for char in x:
            # If the character is an opening symbol, push it onto the stack
            if char in mapping.values():
                stack.append(char)
            # If the character is a closing symbol
            elif char in mapping.keys():
                # If the stack is empty or the top of the stack does not match the corresponding opening symbol, return False
                if not stack or stack.pop() != mapping[char]:
                    return False
        # If the stack is empty, all symbols have been matched and the expression is balanced
        return not stack