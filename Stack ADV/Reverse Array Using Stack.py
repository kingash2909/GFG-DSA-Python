
class Solution:
    def reverseArray(self,n,arr):
        #code here
        if n <= 1:
            return arr
        
        stack = []  # Stack to hold elements
        
        # Push all elements onto the stack
        for elem in arr:
            stack.append(elem)
        
        # Pop elements from the stack and put them back into the array in reversed order
        for i in range(n):
            arr[i] = stack.pop()