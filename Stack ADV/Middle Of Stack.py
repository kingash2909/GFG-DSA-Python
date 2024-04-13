class Solution:
    def stackMiddle(self,n,stack):
        #code here
        if n == 0:
            return None
        
        aux_stack = []  # Auxiliary stack to hold elements
        
        # Move half of the elements to the auxiliary stack
        for _ in range(n // 2):
            aux_stack.append(stack.pop())
        
        # Get the middle element
        middle_element = stack[-1]
        
        # Move elements back to the original stack
        while aux_stack:
            stack.append(aux_stack.pop())
        
        return middle_element