#User function Template for python3

class Solution:
    #Function to count the number of different ways in which n can be 
    #written as a sum of two or more positive integers.
    def countWays(self,n):
       
        mod = 1000000007
        # code here
        dp = [0] * (n + 1)
        
        # Base case: There's only one way to sum up to 0, which is by not selecting any positive integer
        dp[0] = 1
        
        # Iterate from 1 to n (inclusive)
        for i in range(1, n + 1):
            # For each i, calculate the number of ways to sum up to i by considering all possible ways
            for j in range(i, n + 1):
                # Update dp[j] by adding the number of ways to sum up to (j - i)
                dp[j] = (dp[j] + dp[j - i]) % mod
        
        # Return the number of ways to sum up to n
        return (dp[n] - 1) % mod  # Exclude the case where all numbers are 1

