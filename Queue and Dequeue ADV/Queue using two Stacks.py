#User function Template for python3

#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    stack1.append(x) 
    
    
#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if stack2:
        return stack2.pop()
    # If stack2 is empty, transfer elements from stack1 to stack2
    # and then pop from stack2
    elif stack1:
        while stack1:
            stack2.append(stack1.pop())
        return stack2.pop()
    else:
        return -1