

class Solution:
    #Function to find the minimum number of coins to make the change 
    #for value using the coins of given denominations.
    def minimumNumberOfCoins(self,coins,numberOfCoins,value):
        
        # your code here
        dp = [float('inf')] * (value + 1)
        dp[0] = 0
    
        # Iterate over each coin denomination
        for coin in coins:
            # Update dp array for each amount from coin to value
            for i in range(coin, value + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
        # Check if it's possible to make the exact value
        if dp[value] == float('inf'):
            return -1
        else:
            return dp[value]