#Function to push all the elements into the stack.
def _push(a,n):

    # code here
    stack = []
    min_val = float('inf')
    for i in range(n):
        min_val = min(min_val, a[i])
        stack.append(min_val)
    return stack

#Function to print minimum value in stack each time while popping.    
def _getMinAtPop(stack):
    
    # code here
    while stack:
        print(stack.pop(), end=" ")