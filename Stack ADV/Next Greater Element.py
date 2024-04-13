class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        result = [-1] * n  # Initialize result list with -1
        stack = []  # Stack to store indices of elements

        for i in range(n):
            # Keep popping elements from stack while stack is not empty
            # and the current element is greater than the element at the index
            while stack and arr[stack[-1]] < arr[i]:
                result[stack.pop()] = arr[i]  # Set the next greater element

            stack.append(i)  # Push the current index to the stack

        return result