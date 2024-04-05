
#Function to push an element into the stack.
def insert(stack,x):
    # code here
    stack.append(x)
 
#Function to remove top element from stack.
def remove(stack):
    #code here
    if stack:
        return stack.pop()
    else:
        return -1  # Stack is empty
    
#Function to print the top element of stack.    
def headOf_Stack(stack):
    #code here
    if stack:
        return stack[-1]
    else:
        return -1  # Stack is empty
    
#Function to search an element in the stack.
def find(stack,x):
    #code here
    return x in stack