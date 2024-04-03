
class Solution:
    
    #Function to insert all elements of the array in deque.
    def deque_Init(self,arr,n):
        #code here
        # Create a deque
        dq = deque()
    
        # Insert all elements of the array into the deque
        for num in arr:
            dq.append(num)
    
        return dq