
class Solution:
    def postToInfix(self, postfix):
        # Code here
        stack = []  # Initialize an empty stack to store operands and intermediate infix expressions
        # Iterate through each character in the postfix expression
        for char in postfix:
            # If the current character is an operand (i.e., a letter)
            if char.isalpha():
                # Push it onto the stack
                stack.append(char)
            else:
                # Otherwise, the current character is an operator
                # Pop two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()
                # Concatenate them with the operator to form an infix expression
                infix_exp = '(' + operand1 + char + operand2 + ')'
                # Push the infix expression onto the stack
                stack.append(infix_exp)
        # The final infix expression will be on the top of the stack
        return stack[-1]