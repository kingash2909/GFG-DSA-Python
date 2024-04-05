
class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here

        # Helper function to return the precedence of operators
        def precedence(op):
            if op == '^':
                return 3
            elif op == '*' or op == '/':
                return 2
            elif op == '+' or op == '-':
                return 1
            else:
                return -1

        # Initialize an empty stack for operators and an empty list for the postfix expression
        stack = []
        postfix = []

        # Iterate through each character in the infix expression
        for char in exp:
            # If the character is an operand, add it to the postfix expression list
            if char.isalnum():
                postfix.append(char)
            # If the character is an opening parenthesis, push it onto the stack
            elif char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop operators from the stack and add them to the postfix expression until an opening parenthesis is encountered
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove the opening parenthesis from the stack
            # If the character is an operator
            else:
                # Pop operators from the stack and add them to the postfix expression if they have higher precedence than the current operator
                while stack and precedence(stack[-1]) >= precedence(char):
                    postfix.append(stack.pop())
                # Push the current operator onto the stack
                stack.append(char)

        # Pop any remaining operators from the stack and add them to the postfix expression
        while stack:
            postfix.append(stack.pop())

        # Join the elements of the postfix expression list to form a string and return it
        return ''.join(postfix)
