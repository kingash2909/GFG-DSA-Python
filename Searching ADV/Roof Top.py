class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self,A, N):
        #Your code here
        max_steps = 0
        current_steps = 0
        for i in range(1, N):
            if A[i] > A[i - 1]:
                current_steps += 1
            else:
                max_steps = max(max_steps, current_steps)
                current_steps = 0
        max_steps = max(max_steps, current_steps)
        return max_steps