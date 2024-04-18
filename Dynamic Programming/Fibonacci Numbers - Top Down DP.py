

class Solution:
    #Function to find the nth fibonacci number using top-down approach.
    def findNthFibonacci(self,number, dp):
        # Your Code Here
        
        if number <= 0:
            return 0
        elif number == 1 or number == 2:
            return 1
        
        # Initialize dp array to store computed Fibonacci numbers
        dp[1] = 1  # First Fibonacci number
        dp[2] = 1  # Second Fibonacci number
        
        # Compute Fibonacci numbers bottom-up
        for i in range(3, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Return the nth Fibonacci number
        return dp[number]
        