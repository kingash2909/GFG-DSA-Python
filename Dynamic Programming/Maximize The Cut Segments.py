
class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [float('-inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if i - x >= 0:
                dp[i] = max(dp[i], dp[i - x] + 1)
            if i - y >= 0:
                dp[i] = max(dp[i], dp[i - y] + 1)
            if i - z >= 0:
                dp[i] = max(dp[i], dp[i - z] + 1)

        if dp[n] < 0:
            return 0
        else:
            return dp[n]