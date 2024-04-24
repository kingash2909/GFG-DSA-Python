
class Solution:
    
    #Function to find out the number of ways to use the coins to
    #sum up to a certain required value.
    def numberOfWays(self,coins,numberOfCoins,value):
        dp=[0]*(value+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,value+1):
                dp[j]+=dp[j-coin]
        return dp[value]


