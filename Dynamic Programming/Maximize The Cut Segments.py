class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp = [0 for i in range(n)] + [1]
        cuts = tuple(set([x,y,z]))
        
        # print(cuts)
        if 1 in cuts: return n
        if min(cuts) > n: return 0
        if min(cuts) == n: return 1
        
        for i in range(n-min(cuts),-1,-1):
            for j in cuts:
                if i+j <= n and dp[i+j] > 0: dp[i] = max(dp[i], dp[i+j]+1)
            
            
        return dp[0]-1 if dp[0] != 0 else 0s